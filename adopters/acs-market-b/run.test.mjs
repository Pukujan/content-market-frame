import test from "node:test";
import assert from "node:assert/strict";
import {readFileSync} from "node:fs";
import {fileURLToPath} from "node:url";
import {resolve,dirname,join} from "node:path";
import {adaptPrompt,parseArgs,describeTask,SITE_DATA_ACCESS} from "./run.mjs";
const here=dirname(fileURLToPath(import.meta.url));
const spec=readFileSync(join(here,"SPEC.md"),"utf8");

test("ACS B spec is ready as input while primary CTA stays unchosen",()=>{
  const r=describeTask({spec,abaRoot:"ABA_REPO",out:"isolated/acs-b"});
  assert.match(r.spec_sha256,/^[a-f0-9]{64}$/);
  assert.equal(r.deployment_authorized,false);
  assert.equal(r.site_generated,false);
  for(const role of ["ACS","PCM","OIO","CGM"])assert.ok(spec.includes(role),role);
  assert.match(spec,/No primary CTA\./);
  assert.match(spec,/not independently measured customer research/);
});
test("consumer adapter swaps unrelated analytics contract, leaves rest untouched",()=>{
  const analytics="# Data access\nGET /api/views/v_own_posts_latest";
  const original="Header\n"+analytics+"\nFooter";
  const changed=adaptPrompt(original,analytics);
  assert.ok(changed.startsWith("Header\n"));
  assert.ok(changed.endsWith("\nFooter"));
  assert.ok(changed.includes(SITE_DATA_ACCESS));
  assert.ok(!changed.includes("GET /api/views"));
});
test("missing upstream prompt match fails closed rather than silently leaving analytics API",()=>{
  assert.throws(()=>adaptPrompt("new ABA prompts","old data block"),/contract changed/);
});
test("inspection and execution require explicit distinct flags",()=>{
  assert.deepEqual(parseArgs(["--aba","/repo/aba","--out","/tmp/acs-b","--inspect"]),
    {aba:"/repo/aba",out:"/tmp/acs-b",inspect:true});
  assert.throws(()=>parseArgs(["--aba"]),/Missing value/);
});
test("consumer task describes source-first product, real generator and no fake build",()=>{
  assert.match(spec,/source-backed|Source references/);
  assert.match(spec,/ABA consumer/);
  assert.match(spec,/React\/Vite/);
  assert.doesNotMatch(spec,/--require-full-dyad/);
});
