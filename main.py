import sys

def fuzz_bizz(n=100):
    for i in range(1, n + 1):
        parts = []
        if i % 3 == 0:
            parts.append("fuzz")
        if i % 5 == 0:
            parts.append("bizz")
        print(" ".join(parts) if parts else i)

if __name__ == "__main__":
    try:
        n = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    except ValueError:
        n = 100
    fuzz_bizz(n)