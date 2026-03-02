from octagon import octagon

def main():
    octagon_storona=octagon(float(input('длина стороны октагона: ')))
    octagon_storona.vpis_okr()
    octagon_storona.opis_okr()
    octagon_storona.perim_and_sq_okt() 
    octagon_storona.draw_oct()
    
if __name__ == '__main__':
    main()
