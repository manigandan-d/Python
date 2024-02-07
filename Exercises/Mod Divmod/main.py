divident = int(input())
divisor = int(input())

res = divmod(divident, divisor)

print(f"Quotient: {res[0]}")
print(f"Remainder: {res[1]}")
print(f"Result: {res}")

# sample input
# 177
# 10