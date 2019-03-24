tf = [RaNum(0,1)] * max(len(self.x), len(v.x))
            tg = deepcopy(tf)
            th = [RaNum()] * 2 * len(tf)
            for i in range(0,len(self.x)):
                tf[i] = (self.x)[i]
            for i in range(0, len(v.x)):
                tg[i] = (v.x)[i]
            for i in range(0, len(tf)):
                for j in range(0, i):
                    th[i] += tf[j] * tg[i-j]
            tmp = Polynomial(th)
            tmp.Recom()
            return tmp