def doubles(num):
  for counter in range(1,31):
    msg = "Day {} = ${}".format(counter, num)
    print(msg)
    num *= 2

print("If you doubled a penny everyday for a month, you'd be rich after just 1 month.")
doubles(float(input("Pick a currency amount and see how much it would be after 30 days of doubling everyday: ")))
