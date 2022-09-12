from .models import *


class Quary():

    def getoneclothes(self, USERID,value,ClotheName, Type, Color):
        try:
            if value !=0:
                print("----------------------------------")
                print(ClotheName)
                print(Type)
                print(Color)
                print("----------------------------------")

                queryset = HomeModel.objects.filter(
                    USERID=USERID,
                    ClotheName=ClotheName,
                    Type=Type,
                    Color=Color
                )
                if queryset:
                    print(queryset[0].ClotheName, "  ", ClotheName)
                    print(queryset[0].Type, "  ", Type)
                    print(queryset[0].Color, "  ", Color)
                if queryset:
                    if str(queryset[0].ClotheName)== ClotheName:
                        print(queryset[0].ClotheName ,"  ",ClotheName )
                        print(queryset[0].Image)
                    if str(queryset[0].Type)== Type:
                        print(queryset[0].Type, "  ", Type)
                        print(queryset[0].Image)
                    if str(queryset[0].Color)== Color:
                        print(queryset[0].Color, "  ", Color)
                        print(queryset[0].Image)

                return queryset
        except ValueError as e:
            raise Exception('Invalid json: {}'.format(e))

    def validQuery(self, result, Userid, i):
        acceptQuery1 = self.getoneclothes(Userid,result[i].trousers ,'Trousers',
                                          result[i].typetrousers, result[i].colortrousers)

        acceptQuery2 = self.getoneclothes(Userid,result[i].shirt,'Shirt',
                                          result[i].typeShirt, result[i].colorShirt)


        return acceptQuery1, acceptQuery2

    def validQuery1(self, result, Userid, i):
        acceptQuery1 = self.getoneclothes(Userid,result[i].trousers,'Trousers',
                                          result[i].typetrousers, result[i].colortrousers)
        acceptQuery2 = self.getoneclothes(Userid,result[i].T_Shirt,'T_Shirt',
                                          result[i].typeShirt, result[i].colorShirt)
        return acceptQuery1, acceptQuery2

    def validQuery2(self, result, Userid, i):
        acceptQuery1 = self.getoneclothes(Userid,result[i].skirt,'skirt',
                                          result[i].typeSkirt, result[i].colorSkirt)
        acceptQuery2 = self.getoneclothes(Userid,result[i].shirt,'Shirt',
                                          result[i].typeShirt, result[i].colorShirt)
        return acceptQuery1, acceptQuery2

    def validQuery3(self, result, Userid, i):
        acceptQuery1 = self.getoneclothes(Userid,result[i].skirt,'skirt',
                                          result[i].typeSkirt, result[i].colorSkirt)

        acceptQuery2 = self.getoneclothes(Userid,result[i].T_Shirt,'T_Shirt',
                                          result[i].typeShirt, result[i].colorShirt)
        return acceptQuery1, acceptQuery2

    def validQuery4(self, result, Userid, i):
        Dress = self.getoneclothes(Userid,result[i].dress,'dress',
                                   result[i].typeDress, result[i].colorDress)
        Shoes = self.getoneclothes(Userid, result[i].shoes, 'shose',
                                   result[i].typeShoes, result[i].colorShoes)
        return Dress,Shoes

    def validQuery5(self, result, Userid, i):

        Dress = self.getoneclothes(Userid,result[i].dress,'dress',
                                   result[i].typeDress, result[i].colorDress)
        Shoes = self.getoneclothes(Userid, result[i].shoes, 'shose',
                                   result[i].typeShoes, result[i].colorShoes)
        return Dress,Shoes

    def validQuery6(self, result, Userid, i):
        Jacket = self.getoneclothes(Userid,result[i].Jacket,'Jacket',
                                    result[i].typeJacket, result[i].colorJacket)
        Shirt = self.getoneclothes(Userid,result[i].shirt,'Shirt',
                                   result[i].typeShirt, result[i].colorShirt)


        return Jacket,Shirt
    def validQuery7(self, result, Userid, i):
        Jacket = self.getoneclothes(Userid,result[i].Jacket,'Jacket',
                                    result[i].typeJacket, result[i].colorJacket)
        Trousers = self.getoneclothes(Userid,result[i].trousers, 'Trousers',
                                      result[i].typetrousers, result[i].colortrousers)

        return Jacket,Trousers



    def validQuery8(self, result, Userid, i):
        Jacket = self.getoneclothes(Userid,result[i].Jacket,'Jacket',
                                    result[i].typeJacket, result[i].colorJacket)
        Skirt = self.getoneclothes(Userid,result[i].skirt,'skirt',
                                   result[i].typeSkirt, result[i].colorSkirt)


        return Jacket,Skirt


    def validQuery9(self, result, Userid, i):
        Coat = self.getoneclothes(Userid,result[i].coat,'Coat',
                                  result[i].typeCoat, result[i].colorCoats)
        Shoes = self.getoneclothes(Userid,result[i].shoes,'shose',
                                   result[i].typeShoes, result[i].colorShoes)

        return Coat,Shoes




    def allQuery(self, result, Userid, i):
        querset = []
        Shirt = self.getoneclothes(Userid,result[i].shirt,'Shirt',
                                   result[i].typeShirt, result[i].colorShirt)
        querset.append(Shirt)

        Trousers = self.getoneclothes(Userid,result[i].trousers, 'Trousers',
                                      result[i].typetrousers, result[i].colortrousers)
        querset.append(Trousers)


        T_Shirt = self.getoneclothes(Userid,result[i].T_Shirt,'T_Shirt',
                                     result[i].typeT_Shirt, result[i].colorT_Shirt)
        querset.append(T_Shirt)


        Skirt = self.getoneclothes(Userid,result[i].skirt,'skirt',
                                   result[i].typeSkirt, result[i].colorSkirt)
        querset.append(Skirt)


        Dress = self.getoneclothes(Userid,result[i].dress,'dress',
                                   result[i].typeDress, result[i].colorDress)
        querset.append(Dress)
        Shoes = self.getoneclothes(Userid,result[i].shoes,'shose',
                                   result[i].typeShoes, result[i].colorShoes)
        querset.append(Shoes)

        Coat = self.getoneclothes(Userid,result[i].coat,'Coat',
                                  result[i].typeCoat, result[i].colorCoats)
        querset.append(Coat)

        Hat = self.getoneclothes(Userid,result[i].Hat,'Hat',
                                 result[i].typeHat, result[i].colorHat)
        querset.append(Hat)


        Carafe = self.getoneclothes(Userid,result[i].carafe,'carafe',
                                    result[i].typecarafe, result[i].colorcarafe)
        querset.append(Carafe)


        Jacket = self.getoneclothes(Userid,result[i].Jacket,'Jacket',
                                    result[i].typeJacket, result[i].colorJacket)
        querset.append(Jacket)


        Waistband = self.getoneclothes(Userid, result[i].waistband ,'waistband',
                                       result[i].typewaistband, result[i].colorwaistband)
        querset.append(Waistband)

        Formal_suit = self.getoneclothes(Userid,result[i].formal_suit,'formal_suit',
                                         result[i].typeformal_suit, result[i].colorformal_suit)
        querset.append(Formal_suit)

        Graduation_gown = self.getoneclothes(Userid,result[i].graduation_gown, 'graduation_gown',
                                             result[i].typegraduation_gown, result[i].colorgraduation_gown)
        querset.append(Graduation_gown)
        return querset

    def getpath(self, querset):
        solaution = []
        for i in range(len(querset)):
            if querset[i]:
                solaution.append("media/" + str(querset[i][0].Image))
        return solaution

    def getpathAndName(self, querset):
        solaution = []
        for i in range(len(querset)):
            if querset[i]:
                solaution.append(["media/" + str(querset[i][0].Image), str(querset[i][0].ClotheName)])
                print( str(querset[i][0].Image),"              ", str(querset[i][0].ClotheName))
        return solaution

    def getpathAndNamethrid(self, querset,imagepathnew):
        solaution = []
        solaution.append(["media/" + str(imagepathnew), str("imagepathnew")])
        for i in range(len(querset)):

            if querset[i]:
                solaution.append(["media/" + str(querset[i][0].Image), str(querset[i][0].ClotheName)])
                print( str(querset[i][0].Image),"              ", str(querset[i][0].ClotheName))
        return solaution

