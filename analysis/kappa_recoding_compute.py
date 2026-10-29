#!/usr/bin/env python3
"""Cohen's κ for the pre-registered 20% blind re-coding (16 works × 10 decisions)."""
import csv, json, sys
from collections import Counter

def cohen_kappa(a, b):
    assert len(a) == len(b) and len(a) > 0
    n = len(a)
    po = sum(1 for x, y in zip(a, b) if x == y) / n
    cats = set(a) | set(b)
    ca, cb = Counter(a), Counter(b)
    pe = sum((ca[c]/n) * (cb[c]/n) for c in cats)
    if pe == 1.0:
        return (1.0 if po == 1.0 else 0.0), po, pe, "degenerate (one category; perfect agreement)" if po==1.0 else "degenerate"
    return (po - pe) / (1 - pe), po, pe, ""

def main():
    rows = {r['work_id']: r for r in csv.DictReader(open('/Users/mark/随笔/practice-fitting-theory/analysis/corpus_v1.csv'))}
    coded = {}
    for f in ['/tmp/kappa_coded_A.json', '/tmp/kappa_coded_B.json']:
        for item in json.load(open(f)):
            coded[item['work_id']] = item
    works = sorted(coded)
    print(f"配对作品数: {len(works)}")
    if len(works) != 16: print("警告：非 16 篇", file=sys.stderr)

    fields = {'A1': [], 'A2': []}
    for i in range(8): fields[f'D{i+1}'] = []
    orig_flat, new_flat, names_flat = [], [], []
    disagrees = []
    for w in works:
        o, c = rows[w], coded[w]
        pairs = [('A1', o['A1'], c['A1']), ('A2', o['A2'], c['A2'])]
        for i in range(8):
            pairs.append((f'D{i+1}', o['D'][i], c['D'][i]))
        for name, ov, nv in pairs:
            fields[name].append((ov, nv))
            orig_flat.append(ov); new_flat.append(nv); names_flat.append(f"{w}:{name}")
            if ov != nv:
                disagrees.append((w, name, ov, nv, c.get('notes','')[:60]))

    print(f"\n{'字段':<5}{'κ':>8}{'一致率':>8}{'pe':>8}  备注")
    fam = {'A 轴': [], 'D 轴': []}
    for name, plist in fields.items():
        a = [x for x,_ in plist]; b = [y for _,y in plist]
        k, po, pe, note = cohen_kappa(a, b)
        print(f"{name:<5}{k:>8.3f}{po:>8.3f}{pe:>8.3f}  {note}")
        fam['A 轴' if name[0]=='A' else 'D 轴'].extend(plist)
    print()
    for fname, plist in fam.items():
        a = [x for x,_ in plist]; b = [y for _,y in plist]
        k, po, pe, note = cohen_kappa(a, b)
        print(f"{fname} 合并: κ={k:.3f} (po={po:.3f}, n={len(plist)})")
    k, po, pe, note = cohen_kappa(orig_flat, new_flat)
    print(f"\n★ 总体 κ = {k:.3f}  (po={po:.3f}, 判定数={len(orig_flat)}, 门槛 0.70: {'达标' if k>=0.70 else '未达标'})")
    print(f"\n分歧清单 ({len(disagrees)} 处):")
    for w, name, ov, nv, nt in disagrees:
        print(f"  {w} {name}: 原={ov} / 新={nv}  {nt}")

if __name__ == '__main__':
    main()
