# from .QueryDatabase import Quary
from Core.models import *
import json


class searchAll:

    def selectfromDataAndRule(self, query, result, Userid):
        Allresult = {}

        Allresult["USERID"] = Userid
        i=0
        for i in range(len(result)):

            if  result[i].shirt !=0 and result[i].trousers !=0:
                print("Aya")
                acceptQuery1, acceptQuery2 = query.validQuery(result, Userid, i)
                if  acceptQuery2:
                    print(result[i].shoes )
                    print(result[i].colorShoes )
                    print(result[i].typeShoes )
                    print("8888888888888888888888888888888888888")
                    allQuery = query.allQuery(result, Userid, i)
                    allpath = query.getpath(allQuery)

                    if len(allpath) != 0:
                        Allresult["solution" + str(i)] = allpath




            elif result[i].trousers !=0 and result[i].T_Shirt !=0:
                acceptQuery1, acceptQuery2 = query.validQuery1(result, Userid, i)
                allpath = []
                if acceptQuery1 and acceptQuery2:
                    allQuery = query.allQuery(result, Userid, i)
                    allpath = query.getpath(allQuery)
                Allresult["solution" + str(i)] = allpath


            elif result[i].skirt !=0 and result[i].shirt !=0:

                acceptQuery1, acceptQuery2 = query.validQuery2(result, Userid, i)
                allpath = []
                if acceptQuery1 and acceptQuery2:
                    # print("ddd ",i)
                    allQuery = query.allQuery(result, Userid, i)
                    allpath = query.getpath(allQuery)
                    if len(allpath) != 0:
                        Allresult["solution" + str(i)] = allpath



            elif result[i].skirt !=0 and result[i].T_Shirt !=0:
                # print("3", True)
                acceptQuery1, acceptQuery2 = query.validQuery3(result, Userid, i)
                allpath = []
                if acceptQuery1 and acceptQuery2:
                    # print("ddd ",i)
                    allQuery = query.allQuery(result, Userid, i)
                    allpath = query.getpath(allQuery)
                    if len(allpath) != 0:
                        Allresult["solution" + str(i)] = allpath



            elif result[i].dress !=0:
                acceptQuery1 = query.validQuery4(result, Userid, i)
                allpath = []
                if acceptQuery1:
                    allQuery = query.allQuery(result, Userid, i)
                    allpath = query.getpath(allQuery)
                if len(allpath) != 0:
                    Allresult["solution" + str(i)] = allpath

                # else:

        return Allresult

    #
    #
    # def selectfromDataAndRuleSecond(self,query, result,Userid,nameCloth):
    #     Allresult = {}
    #
    #     Allresult["USERID"] = Userid
    #
    #     for i in range(len(result)):
    #
    #         if result[i].trousers and result[i].shirt:
    #
    #             acceptQuery1, acceptQuery2 = query.validQuery(result, Userid, i)
    #
    #             if acceptQuery1 and acceptQuery2:
    #
    #                 allQuery = query.allQuery(result, Userid, i)
    #                 allpath = query.getpathAndName(allQuery)
    #                 index=""
    #
    #                 for i in range(len(allpath)):
    #                     print("ddddddddddddddddddddddddddddddddddddddddd", allpath[i][1])
    #                     print(i)
    #                     print(allpath[i][0])
    #                     if allpath[i][1] == nameCloth:
    #                         index=allpath.index(allpath[i])
    #                         print("uuuuuuuuuuuuuuuuuuuuuuuuu",index)
    #                 allpath.pop(index)
    #
    #                         # allpath.remove(allpath[i][1])
    #             allpathsnew = [allpath[i][0] for i in range(len(allpath))]
    #             print(allpathsnew)
    #             if len(allpathsnew) != 0:
    #                 Allresult["solution" + str(i)] = allpathsnew
    #
    #
    #
    #
    #         elif result[i].trousers and result[i].T_Shirt:
    #             # print("2", True)
    #             acceptQuery1, acceptQuery2 = query.validQuery1(result, Userid, i)
    #             allpath = []
    #             if acceptQuery1 and acceptQuery2:
    #                 # print("ddd ",i)
    #                 allQuery = query.allQuery(result, Userid, i)
    #                 allpath = query.getpathAndName(allQuery)
    #             #     for i in range(len(allpath)):
    #             #         if allpath[i][1] == nameCloth:
    #             #             allpath.remove(allpath[i])
    #             # allpathsnew = [allpath[i][0] for i in range(len(allpath))]
    #             # if len(allpathsnew) != 0:
    #             #     Allresult["solution" + str(i)] = allpathsnew
    #
    #
    #         elif result[i].skirt and result[i].shirt:
    #             # print("3", True)
    #             acceptQuery1, acceptQuery2 = query.validQuery2(result, Userid, i)
    #             allpath = []
    #             if acceptQuery1 and acceptQuery2:
    #                 # print("ddd ",i)
    #                 allQuery = query.allQuery(result, Userid, i)
    #                 allpath = query.getpagetpathAndNameth(allQuery)
    #             #     for i in range(len(allpath)):
    #             #         if allpath[i][1] == nameCloth:
    #             #             allpath.remove(allpath[i])
    #             # allpathsnew = [allpath[i][0] for i in range(len(allpath))]
    #             # if len(allpathsnew) != 0:
    #             #     Allresult["solution" + str(i)] = allpathsnew
    #
    #
    #
    #         elif result[i].skirt and result[i].T_Shirt:
    #             # print("3", True)
    #             acceptQuery1, acceptQuery2 = query.validQuery3(result, Userid, i)
    #             allpath = []
    #             if acceptQuery1 and acceptQuery2:
    #                 # print("ddd ",i)
    #                 allQuery = query.allQuery(result, Userid, i)
    #                 allpath = query.getpathAndName(allQuery)
    #             #     for i in range(len(allpath)):
    #             #         if allpath[i][1] == nameCloth:
    #             #             allpath.remove(allpath[i])
    #             # allpathsnew = [allpath[i][0] for i in range(len(allpath))]
    #             # if len(allpathsnew) != 0:
    #             #     Allresult["solution" + str(i)] = allpathsnew
    #
    #
    #
    #         elif result[i].dress:
    #             acceptQuery1 = query.validQuery4(result, Userid, i)
    #             allpath = []
    #
    #             if acceptQuery1:
    #                 allQuery = query.allQuery(result, Userid, i)
    #                 allpath = query.getpath(allQuery)
    #             #     for i in range(len(allpath)):
    #             #         if allpath[i][1]==nameCloth:
    #             #             allpath.remove(allpath[i])
    #             # allpathsnew=[allpath[i][0] for i in range(len(allpath)) ]
    #             # if len(allpathsnew) != 0:
    #             #     Allresult["solution" + str(i)] = allpathsnew
    #
    #
    #
    #     return Allresult

    def selectfromDataAndRuleSecond(self, query,namecloth,result, Userid, nameClothnew):
        Allresult = {}
        print("nnnnnnnnnnnnnnnnnnnnnnnnnn ",namecloth)

        Allresult["USERID"] = Userid

        for i in range(len(result)):

            if namecloth=="Trousers":

                acceptQuery1, acceptQuery2 = query.validQuery(result, Userid, i)
                allpath = []
                allpathsnew = []

                if acceptQuery2:
                    allQuery = query.allQuery(result, Userid, i)
                    allpath = query.getpathAndName(allQuery)

                if len(allpath)!=0:
                    allpathsnew = [allpath[i][0] for i in range(len(allpath))]
                    print(allpathsnew)
                if len(allpathsnew) != 0:
                    Allresult["solution" + str(i)] = allpathsnew

            if namecloth=="Shirt":

                acceptQuery1, acceptQuery2 = query.validQuery(result, Userid, i)
                allpath = []
                allpathsnew=[]

                if acceptQuery1:
                    allQuery = query.allQuery(result, Userid, i)
                    allpath = query.getpathAndName(allQuery)

                if len(allpath)!=0:
                    allpathsnew = [allpath[i][0] for i in range(len(allpath))]
                    print(allpathsnew)
                if len(allpathsnew) != 0:
                    Allresult["solution" + str(i)] = allpathsnew


            if namecloth=="Trousers":
                acceptQuery1, acceptQuery2 = query.validQuery1(result, Userid, i)
                allpath = []
                allpathsnew = []
                if acceptQuery2:
                    allQuery = query.allQuery(result, Userid, i)
                    allpath = query.getpathAndName(allQuery)

                if len(allpath)!=0:
                    allpathsnew = [allpath[i][0] for i in range(len(allpath))]
                    print(allpathsnew)
                if len(allpathsnew) != 0:
                    Allresult["solution" + str(i)] = allpathsnew


            if namecloth=="T_Shirt":
                acceptQuery1, acceptQuery2 = query.validQuery1(result, Userid, i)
                allpath = []
                allpathsnew = []
                if acceptQuery1:
                    allQuery = query.allQuery(result, Userid, i)
                    allpath = query.getpathAndName(allQuery)

                if len(allpath)!=0:
                    allpathsnew = [allpath[i][0] for i in range(len(allpath))]
                    print(allpathsnew)
                if len(allpathsnew) != 0:
                    Allresult["solution" + str(i)] = allpathsnew


            if namecloth=="skirt":
                acceptQuery1, acceptQuery2 = query.validQuery2(result, Userid, i)
                allpath = []
                allpathsnew = []
                if acceptQuery2:
                    allQuery = query.allQuery(result, Userid, i)
                    allpath = query.getpathAndName(allQuery)
                    print(allpath)

                if len(allpath)!=0:
                    allpathsnew = [allpath[i][0] for i in range(len(allpath))]
                    print(allpathsnew)
                if len(allpathsnew) != 0:
                    Allresult["solution" + str(i)] = allpathsnew

            if namecloth=="Shirt":
                acceptQuery1, acceptQuery2 = query.validQuery2(result, Userid, i)
                allpath = []
                allpathsnew = []
                if acceptQuery1:
                    allQuery = query.allQuery(result, Userid, i)
                    allpath = query.getpathAndName(allQuery)
                    print(allpath)
                if len(allpath)!=0:
                    allpathsnew = [allpath[i][0] for i in range(len(allpath))]
                    print(allpathsnew)
                if len(allpathsnew) != 0:
                    Allresult["solution" + str(i)] = allpathsnew



            if namecloth=="skirt":
                acceptQuery1, acceptQuery2 = query.validQuery3(result, Userid, i)
                allpath = []
                allpathsnew = []
                if acceptQuery2:
                    allQuery = query.allQuery(result, Userid, i)
                    allpath = query.getpathAndName(allQuery)

                if len(allpath) != 0:
                    allpathsnew = [allpath[i][0] for i in range(len(allpath))]
                    print(allpathsnew)
                print(allpathsnew)
                if len(allpathsnew) != 0:
                    Allresult["solution" + str(i)] = allpathsnew


            if namecloth == "T_Shirt":
                acceptQuery1, acceptQuery2 = query.validQuery3(result, Userid, i)
                allpath = []
                allpathsnew = []
                if acceptQuery2:
                    allQuery = query.allQuery(result, Userid, i)
                    allpath = query.getpathAndName(allQuery)

                if len(allpath)!=0:
                    allpathsnew = [allpath[i][0] for i in range(len(allpath))]
                    print(allpathsnew)
                print(allpathsnew)
                if len(allpathsnew) != 0:
                    Allresult["solution" + str(i)] = allpathsnew


            if namecloth == "dress":
                acceptQuery1,acceptQuery2 = query.validQuery5(result, Userid, i)
                allpath = []
                allpathsnew = []

                if acceptQuery2:
                    allQuery = query.allQuery(result, Userid, i)
                    allpath = query.getpath(allQuery)

                if len(allpath)!=0:
                    allpathsnew = [allpath[i][0] for i in range(len(allpath))]
                    print(allpathsnew)

                if len(allpathsnew) != 0:
                    Allresult["solution" + str(i)] = allpathsnew


            if namecloth == "Jacket":
                acceptQuery1,acceptQuery2 = query.validQuery6(result, Userid, i)
                allpath = []
                allpathsnew = []

                if acceptQuery2:
                    allQuery = query.allQuery(result, Userid, i)
                    allpath = query.getpath(allQuery)

                if len(allpath)!=0:
                    allpathsnew = [allpath[i][0] for i in range(len(allpath))]
                    print(allpathsnew)
                if len(allpathsnew) != 0:
                    Allresult["solution" + str(i)] = allpathsnew


            if namecloth == "Shirt":
                acceptQuery1,acceptQuery2 = query.validQuery6(result, Userid, i)
                allpath = []
                allpathsnew = []

                if acceptQuery1:
                    allQuery = query.allQuery(result, Userid, i)
                    allpath = query.getpath(allQuery)

                if len(allpath)!=0:
                    allpathsnew = [allpath[i][0] for i in range(len(allpath))]
                    print(allpathsnew)
                if len(allpathsnew) != 0:
                    Allresult["solution" + str(i)] = allpathsnew


            if namecloth =="Jacket":
                acceptQuery1,acceptQuery2 = query.validQuery7(result, Userid, i)
                allpath = []
                allpathsnew = []

                if acceptQuery2:
                    allQuery = query.allQuery(result, Userid, i)
                    allpath = query.getpath(allQuery)

                if len(allpath)!=0:
                    allpathsnew = [allpath[i][0] for i in range(len(allpath))]
                    print(allpathsnew)
                if len(allpathsnew) != 0:
                    Allresult["solution" + str(i)] = allpathsnew


            if namecloth =="Trousers":
                acceptQuery1,acceptQuery2 = query.validQuery7(result, Userid, i)
                allpath = []
                allpathsnew = []

                if acceptQuery1:
                    allQuery = query.allQuery(result, Userid, i)
                    allpath = query.getpath(allQuery)

                if len(allpath)!=0:
                    allpathsnew = [allpath[i][0] for i in range(len(allpath))]
                    print(allpathsnew)
                if len(allpathsnew) != 0:
                    Allresult["solution" + str(i)] = allpathsnew


            if namecloth =="Jacket":
                acceptQuery1,acceptQuery2 = query.validQuery8(result, Userid, i)
                allpath = []
                allpathsnew = []

                if acceptQuery2:
                    allQuery = query.allQuery(result, Userid, i)
                    allpath = query.getpath(allQuery)

                if len(allpath)!=0:
                    allpathsnew = [allpath[i][0] for i in range(len(allpath))]
                    print(allpathsnew)
                if len(allpathsnew) != 0:
                    Allresult["solution" + str(i)] = allpathsnew


            if namecloth =="Trousers":
                acceptQuery1,acceptQuery2 = query.validQuery8(result, Userid, i)
                allpath = []
                allpathsnew = []

                if acceptQuery1:
                    allQuery = query.allQuery(result, Userid, i)
                    allpath = query.getpath(allQuery)

                if len(allpath)!=0:
                    allpathsnew = [allpath[i][0] for i in range(len(allpath))]
                    print(allpathsnew)
                if len(allpathsnew) != 0:
                    Allresult["solution" + str(i)] = allpathsnew


            if namecloth == "dress":
                acceptQuery1,acceptQuery2 = query.validQuery5(result, Userid, i)
                allpath = []
                allpathsnew = []

                if acceptQuery2:
                    allQuery = query.allQuery(result, Userid, i)
                    allpath = query.getpath(allQuery)

                if len(allpath)!=0:
                    allpathsnew = [allpath[i][0] for i in range(len(allpath))]
                    print(allpathsnew)

                if len(allpathsnew) != 0:
                    Allresult["solution" + str(i)] = allpathsnew

        return Allresult

    def selectfromDataAndRuleThird(self, query, result, Userid, namecloth, imagepath1):
        Allresult = {}
        print("nnnnnnnnnnnnnnnnnnnnnnnnnn ", namecloth)

        Allresult["USERID"] = Userid

        for i in range(len(result)):

            if namecloth == "Trousers":

                acceptQuery1, acceptQuery2 = query.validQuery(result, Userid, i)
                allpath = []
                allpathsnew = []

                if acceptQuery2:
                    allQuery = query.allQuery(result, Userid, i)
                    allpath = query.getpathAndNamethrid(allQuery,imagepath1)


                if len(allpath) != 0:
                    if len(allpath) != 1 and allpath[0][1]== "imagepathnew":
                        allpathsnew = [allpath[i][0] for i in range(len(allpath))]
                        print(allpathsnew)
                if len(allpathsnew) != 0:
                    Allresult["solution" + str(i)] = allpathsnew

            if namecloth == "Shirt":

                acceptQuery1, acceptQuery2 = query.validQuery(result, Userid, i)
                allpath = []
                allpathsnew = []

                if acceptQuery1:
                    allQuery = query.allQuery(result, Userid, i)
                    allpath = query.getpathAndNamethrid(allQuery, imagepath1)


                if len(allpath) != 0:
                    if len(allpath) != 1 and allpath[0][1]== "imagepathnew":
                        allpathsnew = [allpath[i][0] for i in range(len(allpath))]
                        print(allpathsnew)
                if len(allpathsnew) != 0:
                    Allresult["solution" + str(i)] = allpathsnew

            if namecloth == "Trousers":
                acceptQuery1, acceptQuery2 = query.validQuery1(result, Userid, i)
                allpath = []
                allpathsnew = []
                if acceptQuery2:
                    allQuery = query.allQuery(result, Userid, i)
                    allpath = query.getpathAndNamethrid(allQuery, imagepath1)


                if len(allpath) != 0:
                    if len(allpath) != 1 and allpath[0][1]== "imagepathnew":
                        allpathsnew = [allpath[i][0] for i in range(len(allpath))]
                        print(allpathsnew)
                if len(allpathsnew) != 0:
                    Allresult["solution" + str(i)] = allpathsnew

            if namecloth == "T_Shirt":
                acceptQuery1, acceptQuery2 = query.validQuery1(result, Userid, i)
                allpath = []
                allpathsnew = []
                if acceptQuery1:
                    allQuery = query.allQuery(result, Userid, i)
                    allpath = query.getpathAndNamethrid(allQuery, imagepath1)

                if len(allpath) != 0:
                    if len(allpath) != 1 and allpath[0][1]== "imagepathnew":
                        allpathsnew = [allpath[i][0] for i in range(len(allpath))]
                        print(allpathsnew)
                if len(allpathsnew) != 0:
                    Allresult["solution" + str(i)] = allpathsnew

            if namecloth == "skirt":
                acceptQuery1, acceptQuery2 = query.validQuery2(result, Userid, i)
                allpath = []
                allpathsnew = []
                if acceptQuery2:
                    allQuery = query.allQuery(result, Userid, i)
                    allpath = query.getpathAndNamethrid(allQuery, imagepath1)
                    print(allpath)

                if len(allpath) != 0:
                    if len(allpath) != 1 and allpath[0][1]== "imagepathnew":
                        allpathsnew = [allpath[i][0] for i in range(len(allpath))]
                        print(allpathsnew)
                if len(allpathsnew) != 0:
                    Allresult["solution" + str(i)] = allpathsnew

            if namecloth == "Shirt":
                acceptQuery1, acceptQuery2 = query.validQuery2(result, Userid, i)
                allpath = []
                allpathsnew = []
                if acceptQuery1:
                    allQuery = query.allQuery(result, Userid, i)
                    allpath = query.getpathAndNamethrid(allQuery, imagepath1)
                    print(allpath)

                if len(allpath) != 0:
                    if len(allpath) != 1 and allpath[0][1]== "imagepathnew":
                        allpathsnew = [allpath[i][0] for i in range(len(allpath))]
                        print(allpathsnew)
                if len(allpathsnew) != 0:
                    Allresult["solution" + str(i)] = allpathsnew

            if namecloth == "skirt":
                acceptQuery1, acceptQuery2 = query.validQuery3(result, Userid, i)
                allpath = []
                allpathsnew = []
                if acceptQuery2:
                    allQuery = query.allQuery(result, Userid, i)
                    allpath = query.getpathAndNamethrid(allQuery, imagepath1)

                if len(allpath) != 0:
                    if len(allpath) != 1 and allpath[0][1]== "imagepathnew":
                        allpathsnew = [allpath[i][0] for i in range(len(allpath))]
                        print(allpathsnew)
                if len(allpathsnew) != 0:
                    Allresult["solution" + str(i)] = allpathsnew

            if namecloth == "T_Shirt":
                acceptQuery1, acceptQuery2 = query.validQuery3(result, Userid, i)
                allpath = []
                allpathsnew = []
                if acceptQuery2:
                    allQuery = query.allQuery(result, Userid, i)
                    allpath = query.getpathAndNamethrid(allQuery, imagepath1)

                if len(allpath) != 0:
                    if len(allpath) != 1 and allpath[0][1]== "imagepathnew":
                        allpathsnew = [allpath[i][0] for i in range(len(allpath))]
                        print(allpathsnew)
                if len(allpathsnew) != 0:
                    Allresult["solution" + str(i)] = allpathsnew

            if namecloth == "dress":
                acceptQuery1, acceptQuery2 = query.validQuery5(result, Userid, i)
                allpath = []
                allpathsnew = []

                if acceptQuery2:
                    allQuery = query.allQuery(result, Userid, i)
                    allpath = query.getpathAndNamethrid(allQuery, imagepath1)

                if len(allpath) != 0:
                    if len(allpath) != 1 and allpath[0][1]== "imagepathnew":
                        allpathsnew = [allpath[i][0] for i in range(len(allpath))]
                        print(allpathsnew)
                if len(allpathsnew) != 0:
                    Allresult["solution" + str(i)] = allpathsnew

            if namecloth == "Jacket":
                acceptQuery1, acceptQuery2 = query.validQuery6(result, Userid, i)
                allpath = []
                allpathsnew = []

                if acceptQuery2:
                    allQuery = query.allQuery(result, Userid, i)
                    allpath = query.getpathAndNamethrid(allQuery, imagepath1)

                if len(allpath) != 0:
                    if len(allpath) != 1 and allpath[0][1]== "imagepathnew":
                        allpathsnew = [allpath[i][0] for i in range(len(allpath))]
                        print(allpathsnew)
                if len(allpathsnew) != 0:
                    Allresult["solution" + str(i)] = allpathsnew

            if namecloth == "Shirt":
                acceptQuery1, acceptQuery2 = query.validQuery6(result, Userid, i)
                allpath = []
                allpathsnew = []

                if acceptQuery1:
                    allQuery = query.allQuery(result, Userid, i)
                    allpath = query.getpathAndNamethrid(allQuery, imagepath1)

                if len(allpath) != 0:
                    if len(allpath) != 1 and allpath[0][1]== "imagepathnew":
                        allpathsnew = [allpath[i][0] for i in range(len(allpath))]
                        print(allpathsnew)
                if len(allpathsnew) != 0:
                    Allresult["solution" + str(i)] = allpathsnew

            if namecloth == "Jacket":
                acceptQuery1, acceptQuery2 = query.validQuery7(result, Userid, i)
                allpath = []
                allpathsnew = []

                if acceptQuery2:
                    allQuery = query.allQuery(result, Userid, i)
                    allpath = query.getpathAndNamethrid(allQuery, imagepath1)

                if len(allpath) != 0:
                    if len(allpath) != 1 and allpath[0][1]== "imagepathnew":
                        allpathsnew = [allpath[i][0] for i in range(len(allpath))]
                        print(allpathsnew)
                if len(allpathsnew) != 0:
                    Allresult["solution" + str(i)] = allpathsnew

            if namecloth == "Trousers":
                acceptQuery1, acceptQuery2 = query.validQuery7(result, Userid, i)
                allpath = []
                allpathsnew = []

                if acceptQuery1:
                    allQuery = query.allQuery(result, Userid, i)
                    allpath = query.getpathAndNamethrid(allQuery, imagepath1)

                if len(allpath) != 0:
                    if len(allpath) != 1 and allpath[0][1]== "imagepathnew":
                        allpathsnew = [allpath[i][0] for i in range(len(allpath))]
                        print(allpathsnew)
                if len(allpathsnew) != 0:
                    Allresult["solution" + str(i)] = allpathsnew

            if namecloth == "Jacket":
                acceptQuery1, acceptQuery2 = query.validQuery8(result, Userid, i)
                allpath = []
                allpathsnew = []

                if acceptQuery2:
                    allQuery = query.allQuery(result, Userid, i)
                    allpath = query.getpathAndNamethrid(allQuery, imagepath1)

                if len(allpath) != 0:
                    if len(allpath) != 1 and allpath[0][1]== "imagepathnew":
                        allpathsnew = [allpath[i][0] for i in range(len(allpath))]
                        print(allpathsnew)
                if len(allpathsnew) != 0:
                    Allresult["solution" + str(i)] = allpathsnew

            if namecloth == "Trousers":
                acceptQuery1, acceptQuery2 = query.validQuery8(result, Userid, i)
                allpath = []
                allpathsnew = []

                if acceptQuery1:
                    allQuery = query.allQuery(result, Userid, i)
                    allpath = query.getpathAndNamethrid(allQuery, imagepath1)

                if len(allpath) != 0:
                    if len(allpath) != 1 and allpath[0][1]== "imagepathnew":
                        allpathsnew = [allpath[i][0] for i in range(len(allpath))]
                        print(allpathsnew)
                if len(allpathsnew) != 0:
                    Allresult["solution" + str(i)] = allpathsnew

            if namecloth == "dress":
                acceptQuery1, acceptQuery2 = query.validQuery5(result, Userid, i)
                allpath = []
                allpathsnew = []

                if acceptQuery2:
                    allQuery = query.allQuery(result, Userid, i)
                    allpath = query.getpathAndNamethrid(allQuery, imagepath1)

                if len(allpath) != 0:
                    if len(allpath) != 1 and allpath[0][1]== "imagepathnew":
                        allpathsnew = [allpath[i][0] for i in range(len(allpath))]
                        print(allpathsnew)
                if len(allpathsnew) != 0:
                    Allresult["solution" + str(i)] = allpathsnew

        return Allresult

