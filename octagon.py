import math
import matplotlib.pyplot as mp #импорт библиотек

class octagon:

    def __init__(self, storona): #конструктор 
        self.storona = storona
        self.ugol = 2*3.14/8 #угол октогона
        self.k= 1+2**(1/2) #константа
    
    def vpis_okr (self): 
        R_vpis = self.storona/(2*(2**(1/2)-1)) #формула радиуса вписанной окружности
        print(f"радиус вписанной окружности:",{R_vpis})
        S_vpis = (3.14 * (R_vpis**2)) #площадь вписанной окружности
        print(f"площадь вписанной окружности:",{S_vpis})

    def opis_okr (self): 
        R_opis = self.storona/((2-2**(1/2))**(1/2)) #формула радиуса описанной окружности
        print(f"радиус описанной окружности:",{R_opis})
        S_opis = (3.14 * (R_opis**2)) #площадь описанной окружности
        print(f"площадь описанной окружности:",{S_opis})

    def perim_and_sq_okt(self):
        P_okt=self.storona*8 #формула для периметра
        print(f"периметр октагона:",{P_okt})
        S_okt=2*self.storona**2*self.k #формула для площади
        print(f"площадь октагона:",{S_okt})
    

    def draw_oct(self):
        R_vpis = self.storona/(2*(2**(1/2)-1)) #формула радиуса вписанной окружности
        R_opis = self.storona/((2-2**(1/2))**(1/2)) #формула радиуса описанной окружности
        fig, ax = mp.subplots(figsize=(20, 20))  #создаём график и оси https://sky.pro/wiki/media/vyvod-grafikov-matplotlib-v-ipython-notebook/?ysclid=mm9cqmp1o2691985824
        ax.set_aspect('equal') #Установка равного соотношения сторон https://external.software/archives/23129?ysclid=mm9d3ggkuj475114572
        #создаём списки для восьми вершин
        x = [R_opis * math.cos(i * self.ugol) for i in range(10)] 
        y = [R_opis * math.sin(i * self.ugol) for i in range(10)] 
        #чтобы фигура замыкалась
        x.append(x[0])  
        y.append(y[0])
        ax.plot(x,y,color='pink',markersize=10) #розовый октагон
        circle_out = mp.Circle((0, 0), R_opis, color='orange', fill=False, label="описанная окружность" ) #создаем оранжевую описанную без заливки окружность
        ax.add_patch(circle_out) #добавление на график
        circle_in = mp.Circle((0, 0), R_vpis, color='yellow', fill=False, label="вписанная окружность" ) #создаем желтую вписанную без заливки окружность
        ax.add_patch(circle_in) #добавление на график
        mp.legend() #цвета
        mp.show() #вывод графика

    def __del__(self): #деструктор
        print('все удалено')


        
