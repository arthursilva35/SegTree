import random

def gerador_instancias(num_inst: int, tam_min: int, tam_max: int) -> list:
    instancias = []
    
    for _ in range(num_inst): 
        
        tam = random.randint(tam_min, tam_max)
        cur_inst = []  
        
        for _ in range(tam):
            cur_inst.append(random.randint(-100, 100))

        instancias.append(cur_inst)

    return instancias


if __name__ == '__main__':

    instancias = gerador_instancias(10, 5, 50)


    print(len(instancias))

    for i in range(len(instancias)):
        cur_inst = instancias[i] 
        
        tam = len(cur_inst)
        
        out_str = "("
        
        for j in range(tam):
            if j == (tam - 1):         
                out_str += str(cur_inst[j]) + ")"
            else:
                out_str += str(cur_inst[j]) + ", "

        print(out_str)
