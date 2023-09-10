def gen(index):
  months=['jan','feb','mar','apr','may','june','july','aug','sep','oct','nov','dec']
  yield months(index)
  yield months(index+2)

next_month=gen(3)
print(next(next_month),next(next_month))

#output
#apr jun
