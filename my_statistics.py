p = [ 1, 2, 4, 66, 73, 124, 234, 234, 22,]

def my_max(p): #максимальное значение
  return max(p)

def my_min(p): #минимальное зачение
  return min(p)

def my_mean(p): #среднее арифетическое
  return sum(p)/len(p)

def my_median(p): #среднее число
  p.sort()
  n= len(p)
  ind = n//2
  if n % 2 != 0:
    return p[ind]
  else:
    return (p[ind-1] + p[ind]) /2
  
def my_mode(p): #самое часто встречающиеся число
  try:
    import statistics
    return statistics.mode(p)
  except: "нет однозначного ответа"

def my_different(p): #разница
  return max(p) - min(p)

def my_square(p):
  s = 0
  for i in p:
    s += (i - my_mean(p))**2
  return round((s/ (len(p)-1))**0.5, 2)

def my_quartil(p):
  import pandas as dp
  df = dp.Series(p)
  qw = df.quantile([.25, .5, .75])
  z=[]
  for i in qw:
    z.append(i)
  return z

def my_quartil_razmah(p):
  q = my_quartil(p)
  s = []
  for i in p:
    if i > q[0] and i <q[2]:
      s.append(i)
  return s

def my_simetric(p):
  raznost = abs(my_median(p) - my_mean(p))
  if raznost <= 3 * (( my_square(p)/len(p) )**0.5):
    return True
  else:
    return False

