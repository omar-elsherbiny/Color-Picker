def rgb2hsv(R, G, B):
        r,g,b=R/255.0,G/255.0,B/255.0
        cmax,cmin=max(r,g,b),min(r,g,b)
        diff=cmax-cmin

        if cmax==cmin:
            h=0
        elif cmax==r:
            h=(60*((g-b)/diff)+360) % 360
        elif cmax==g:
            h=(60*((b-r)/diff)+120) % 360
        elif cmax==b:
            h=(60*((r-g)/diff)+240) % 360
        
        if cmax==0:
            s=0
        else:
            s=(diff/cmax)*100
        
        v=cmax*100

        return (round(h),round(s),round(v))
def hsv2rgb(H, S, V):
    S/=100
    V/=100
    if S==0:
        V*=255
        return (V,V,V)
    i=int(H*6.)
    f=(H*6.)-i
    p,q,t=round(255*(V*(1.-S))), round(255*(V*(1.-S*f))), round(255*(V*(1.-S*(1.-f))))
    V=round(V*255)
    i=(H*6.)%6
    print(i)
    if i==0: return (V,t,p)
    if i==1: return (q,V,p)
    if i==2: return (p,V,t)
    if i==3: return (p,q,V)
    if i==4: return (t,p,V)
    if i==5: return (V,p,q)

if __name__=='__main__':
    col=(40,80,255)
    h=rgb2hsv(col[0],col[1],col[2])
    r=hsv2rgb(h[0],h[1],h[2])
    print(col)
    print(h)
    print(r)