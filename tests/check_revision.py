"""Compare two versions of data/items.json the way a reviewer would.

    python3 -I tests/check_revision.py BASE_items.json HEAD_items.json

Fails (exit 1) when:
  - an item present in BASE is missing from HEAD (removing an item is a maintainer decision, not a PR default);
  - any BASE caveat no longer survives verbatim inside the HEAD caveat of the same item (caveats are append-only).
Prints every other changed field, and flags the ones that move an item up the ladder or change its label
(verification, contested, llm, physical, quantum, tier, P/H/W/C) so the reviewer looks for the source.
"""
import json, sys

base = {e["id"]: e for e in json.load(open(sys.argv[1], encoding="utf-8"))}
head = {e["id"]: e for e in json.load(open(sys.argv[2], encoding="utf-8"))}
FLAG = ("verification", "contested", "llm", "physical", "quantum", "tier", "P", "H", "W", "C")
failures, flagged, changed = [], [], []

for i, b in base.items():
    h = head.get(i)
    if h is None:
        failures.append(f"{i}: removed")
        continue
    if b["caveat"] not in h.get("caveat", ""):
        failures.append(f"{i}.caveat: text removed or rewritten (caveats are append-only)\n    base: {b['caveat']}\n    head: {h.get('caveat')}")
    for k in sorted(set(b) | set(h)):
        if b.get(k) != h.get(k):
            changed.append(f"{i}.{k}: {json.dumps(b.get(k), ensure_ascii=False)} -> {json.dumps(h.get(k), ensure_ascii=False)}")
            if k in FLAG:
                flagged.append(f"{i}.{k}")
added = [i for i in head if i not in base]

print(f"{len(changed)} field(s) changed, {len(added)} item(s) added {added}, {len(failures)} failure(s)")
for c in changed:
    print("  " + c)
if flagged:
    print("\nNeeds a primary source in the PR (label, flag or rating changed): " + ", ".join(flagged))
if failures:
    print("\nFAIL")
    for f in failures:
        print("  " + f)
    sys.exit(1)
print("\nOK")
