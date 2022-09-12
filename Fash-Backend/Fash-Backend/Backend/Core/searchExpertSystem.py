from .ExpertSys import CLOTHESThird, CLOTHESSecond,Myclothes,CLOTHES,Occasion,age,Person_type,Gender,SkinColor,Season,piece_type,piece_name,piece_color

engine = CLOTHES()
engine2 = CLOTHESSecond()
engine3=CLOTHESThird()


class Search:

    def AllresultFirst(self, result):
        engine.reset()

        engine.declare(age(value=int(result["Age"])), SkinColor(color=result["SkinColor"]),
                       Occasion(result["Occasion"]), Gender(result["Gender"]),
                       Person_type(result["PersonType"]), Season(result["Season"]))
        engine.facts

        engine.run()


        return engine.result


    def AllresultSecond(self, result):

        engine2.reset()

        engine2.declare(age(value=int(result["Age"])), SkinColor(color=result["SkinColor"]),
                       Occasion(result["Occasion"]), Gender(result["Gender"]),
                       Person_type(result["PersonType"]), Season(result["Season"]),piece_name(result["ClotheName"]),
                       piece_type(result["Type"]), piece_color(result["Color"]))
        engine2.facts
        engine2.run()
        return engine2.result


    def AllresultThird(self, result):

        engine3.reset()

        engine3.declare(age(value=int(result["Age"])), SkinColor(color=result["SkinColor"]),
                       Occasion(result["Occasion"]), Gender(result["Gender"]),
                       Person_type(result["PersonType"]), Season(result["Season"]),piece_name(result["ClotheName"]),
                         piece_color(result["Color"]))
        engine3.facts
        engine3.run()

        return engine3.result


result1 = {'Code': 200, 'USERID': 'b490a7e0-fd46-4106-b4fc-462b84259513', 'Season': 'summer', 'Age': '23', 'Gender': 'female',
     'SkinColor': 'white', 'Occasion': 'gradution', 'PersonType': 'student', 'ClotheName': 'Skirt', 'Type': 'MidSkirt',
     'Color': 'black'}


search_=Search()
res=search_.AllresultSecond(result1)
print("ffffff",len(res))
for i in range(len(res)):
    # for j in range(len(res[i])):
    print(res[i].colortrousers)
    print(res[i].typetrousers )
    #  كنزة
    print(res[i]. T_Shirt )
    print(res[i].colorT_Shirt )
    print(res[i].typeT_Shirt )
    #  قميص
    print(res[i].shirt )
    print(res[i].colorShirt )
    print(res[i].typeShirt )
    #  تنورة
    print(res[i].skirt )
    print(res[i].colorSkirt )
    print(res[i].typeSkirt )
    #  حذاء
    print(res[i].shoes )
    print(res[i].colorShoes )
    print(res[i].typeShoes )
    #  معطف
    print(res[i].coat )
    print(res[i]. colorCoats )
    print(res[i]. typeCoat )
    # طاقية
    print(res[i]. Hat )
    print(res[i]. colorHat )
    print(res[i]. typeHat )
    #  كرافة
    print(res[i]. carafe )
    print(res[i].colorcarafe )
    print(res[i].typecarafe )
    #  جاكيت
    print(res[i].Jacket )
    print(res[i].colorJacket )
    print(res[i].typeJacket )
    #
    print(res[i]. dress )
    print(res[i].colorDress )
    print(res[i].typeDress )
    #  حزام
    print(res[i].waistband )
    print(res[i].colorwaistband )
    print(res[i]. typewaistband )

    #  طقم
    print(res[i].formal_suit )
    print(res[i]. colorformal_suit )
    print(res[i].typeformal_suit )
    # عباية تخرج
    print(res[i].graduation_gown )
    print(res[i]. colorgraduation_gown )
    print(res[i] .typegraduation_gown )
    print("/////////////////////////")

