#!/usr/bin/env node
// ACS B is an ABA ADOPTER, not internal Dyad/Pro development.
// Reuses ABA's existing generator; replaces ONLY the unrelated analytics
// data-access contract, following the proven IRE consumer precedent.
import {existsSync} from "node:fs";
import {readFile,writeFile} from "node:fs/promises";
import {resolve,join,dirname} from "node:path";
import {fileURLToPath,pathToFileURL} from "node:url";
import {createHash} from "node:crypto";

const HERE=dirname(fileURLToPath(import.meta.url));
export const SITE_DATA_ACCESS=[
  "# ACS market site data contract — static product introduction",
  "- This is a static informational website, NOT a personal-brand analytics dashboard.",
  "- No SQLite datastore, analytics-view endpoint, authenticated API, agent runtime or installation endpoint is available.",
  "- All product claims must trace to pinned source links in the spec. Do not invent data, customer metrics, testimonials or installation receipts.",
  "- The primary action is unresolved; do not generate an installer or a CTA button. Source-documentation anchors are evidence links only.",
  "- There is no backend or write side effect. Do not simulate a working installer."
].join("\n");

export function parseArgs(argv){
  const args={};
  for(let i=0;i<argv.length;i++){
    const k=argv[i];
    if(!k.startsWith("--"))throw new Error("Unknown positional argument: "+k);
    if(k==="--inspect" || k==="--execute"){args[k.slice(2)]=true;continue;}
    const val=argv[++i];
    if(!val||val.startsWith("--"))throw new Error("Missing value for "+k);
    args[k.slice(2)]=val;
  }
  return args;
}
export function adaptPrompt(prompt,originalAccess){
  if(!originalAccess || !prompt.includes(originalAccess))
    throw new Error("ABA prompt contract changed: cannot locate the exact default DATA_ACCESS block");
  return prompt.replace(originalAccess,SITE_DATA_ACCESS);
}
export function describeTask({spec,abaRoot,out}){
  const required=["data-testid=\"acs-introduction\"","data-testid=\"integrated-components\"",
    "data-testid=\"technical-details\"","No primary CTA."];
  for(const text of required)if(!spec.includes(text))
    throw new Error("ACS B consumer spec is missing contract: "+text);
  return {task:"acs-market-b",spec_sha256:createHash("sha256").update(spec).digest("hex"),
    aba_root:abaRoot,workspace:out,provider_configured:
      Boolean(process.env.BUILDER_API_KEY||process.env.OPENAI_API_KEY||
        process.env.HADES_LITELLM_API_KEY||process.env.OPENCODE_LITELLM_MASTER_KEY),
    model_configured:Boolean(process.env.BUILDER_MODEL),
    deployment_authorized:false,site_generated:false,
    note:"This inspection is a local readiness description, NOT a model run"};
}
async function run(){
  const args=parseArgs(process.argv.slice(2));
  if(!args.aba||!args.out)throw new Error("Usage: node run.mjs --aba <local ABA checkout> --out <fresh directory> [--inspect | --execute]");
  if(Boolean(args.inspect)===Boolean(args.execute))
    throw new Error("Choose exactly one: --inspect or --execute");
  const abaRoot=resolve(args.aba),out=resolve(args.out);
  const specPath=resolve(args.spec||join(HERE,"SPEC.md"));
  const spec=await readFile(specPath,"utf8");
  const task=describeTask({spec,abaRoot,out});
  if(args.inspect){console.log(JSON.stringify(task,null,2));return;}
  // Fail before any workspace write unless this is a new separate directory.
  if(existsSync(out))throw new Error("Refusing to replace existing workspace: "+out);
  const load=name=>import(pathToFileURL(join(abaRoot,"server","src",name)).href);
  const [{loadConfig},{verifyModel,assertModelIdentity},
    {createWorkspace,defaultTemplateDir},{buildSystemPrompt,DATA_ACCESS},{generate}]=await Promise.all([
      load("config.mjs"),load("provider.mjs"),load("workspace.mjs"),
      load("prompts.mjs"),load("loop.mjs")]);
  const cfg=loadConfig({model:args.model});
  const verdict=await verifyModel(cfg);
  assertModelIdentity(cfg,verdict);
  const basePrompt=buildSystemPrompt({spec,workspace:out});
  const systemPrompt=adaptPrompt(basePrompt,DATA_ACCESS);
  await createWorkspace({templateDir:defaultTemplateDir(),outDir:out,force:false});
  const result=await generate({cfg,systemPrompt,spec,workspace:out});
  const receipt={
    schema_version:"acs-b.aba-consumer-run.v1",task:"acs-market-b",
    aba_entrypoint:"server/src/loop.mjs generate()",
    spec_sha256:task.spec_sha256,
    model_requested:cfg.model,model_identity_verified:Boolean(verdict.ok),
    ok:Boolean(result.ok),steps:result.stats?.steps??null,
    tool_calls:result.stats?.toolCalls??null,files_written:result.stats?.filesWritten??null,
    blueprint_written:Boolean(result.blueprint),
    typecheck_passed:Boolean(result.typecheck?.ok),
    completeness_passed:Boolean(result.completeness?.ok),
    deployment_authorized:false,creative_acceptance:"not_established",
    next:"Review actual generated app in browser and obtain independent creative approval; never treat this receipt as deployment permission"
  };
  await writeFile(join(out,"ACS_B_ABA_RECEIPT.json"),JSON.stringify(receipt,null,2)+"\n");
  console.log(JSON.stringify(receipt,null,2));
  if(!result.ok)process.exitCode=1;
}
if(process.argv[1] && resolve(process.argv[1])===fileURLToPath(import.meta.url))
  run().catch(e=>{console.error("ACS B ABA consumer generation error:",e.message);process.exitCode=1;});
