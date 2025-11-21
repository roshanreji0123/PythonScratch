def valid_expression(queries):
    pair = {")":"(", "]":"[", "}":"{"}
    results = []

    for string in queries:
        # Odd length → automatically invalid
        if len(string) % 2 != 0:
            results.append("NO")
            continue

        stack = []
        valid = True

        for ch in string:
            if ch in "({[":
                stack.append(ch)

            elif ch in ")}]":
                if not stack or stack[-1] != pair[ch]:
                    valid = False
                    break
                stack.pop()

            else:
                valid = False
                break

        # After loop, if stack still has items → invalid
        if stack:
            valid = False

        results.append("YES" if valid else "NO")

    return results


# Test:
n=int(input("Enter the  no strings for valid parantheses check"))
queries=[]
for i in range(1,n+1):
    string=input(f"{i}:")
    queries.append(string)
results=valid_expression(queries)
for r in results:
 print(r)
