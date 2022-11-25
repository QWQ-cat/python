for i in range(10):
    t = float(input("溫度"))
    h = float(input("濕度"))
    v = float(input("風速"))
    ssd = (1.818*t+18.18)*(0.88+0.002*h)+(t-32)/(45-t)-(3.2*v)+18.2
    print(ssd)
