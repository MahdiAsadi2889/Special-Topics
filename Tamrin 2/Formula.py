tau = 2
v = 5
vr = 4

def formula(dv_dt):
    dv_dt = (-1/tau)*(v-vr)
    return dv_dt

print(formula(2))