NUM_CACHE_LINES = 8
cache = [None] * NUM_CACHE_LINES
access_sequence = [3, 11, 3, 19, 11, 27, 3]
total_hits = 0
total_misses = 0

print("--- DIRECT-MAPPED CACHE SIMULATION ---")
print(f"Cache Lines: {NUM_CACHE_LINES}")
print(f"Access Sequence: {access_sequence}\n")

print(f"{'Access':<8} | {'Memory Block':<12} | {'Cache Line':<10} | {'Status':<6} | {'Cache Contents'}")
print("-" * 75)

for i, block in enumerate(access_sequence):
    cache_line = block % NUM_CACHE_LINES
    
    if cache[cache_line] == block:
        status = "HIT"
        total_hits += 1
    else:
        status = "MISS"
        total_misses += 1
        cache[cache_line] = block
        
    display_cache = [str(x) if x is not None else '-' for x in cache]
    cache_str = "[" + ", ".join(display_cache) + "]"
    
    print(f"{i+1:<8} | {block:<12} | {cache_line:<10} | {status:<6} | {cache_str}")

total_accesses = len(access_sequence)
hit_ratio = total_hits / total_accesses

print("-" * 75)
print("\n--- FINAL RESULTS ---")
print(f"Total Hits   : {total_hits}")
print(f"Total Misses : {total_misses}")
print(f"Hit Ratio    : {hit_ratio:.2f} (or {hit_ratio * 100:.1f}%)")

