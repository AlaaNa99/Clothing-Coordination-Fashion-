import 'package:dio/dio.dart';
import 'package:flutter/material.dart';
import 'package:login/modules/output/output.dart';
import 'package:login/modules/output/output_second.dart';
import 'package:login/shared/components/components.dart';
import 'package:login/url.dart';
import 'package:shared_preferences/shared_preferences.dart';

class SecoundScreen extends StatefulWidget {
  const SecoundScreen({ Key? key }) : super(key: key);

  @override
  State<SecoundScreen> createState() => _SecoundScreenState();
}

class _SecoundScreenState extends State<SecoundScreen> {
   String trouser = "type";
  List<String> type_trouser = [
    "type",
    "Trousers",
    "wide_pants",
    "jeans",
    "short",
    "pajama"
  ];
  String T_Shirt = "type";
  List<String> type_Tshirt = ["type", "T_Shirt", "Hoodie"];
  String Shirt = "Shirt";
  List<String> type_Shirt = ["Shirt"];
  String Skirt = "skirt";
  List<String> type_skirt = ["skirt", "jeans", "MidSkirt", "shortSkirt"];
  String shoes = "type";
  List<String> type_shose = ["type", "shoes", "Kandra", "Sandal"];
  String Coat = "type";
  List<String> type_coat = ["type", "Coat"];
  String Hat = "type";
  List<String> type_Hat = ["type", "Hat"];
  String carafe = "type";
  List<String> type_corafee = ["type", "carafe"];
  String Jacket = "type";
  List<String> type_jacket = ["type", "Jacket"];
  String dress = "dress";
  List<String> type_dress = ["dress", "Midriff", "Long_robe", "Mididress"];
  String waistband = "type";
  List<String> type_Waistband = ["type", "waistband"];
  String formal_suit = "type";
  List<String> type_Formal_Suit = ["type", "formal_suit", "formal_suit_skirt"];
  String graduation_gown = "type";
  List<String> type_graduation_gown = ["type", "graduation_gown"];
  String clothes_ = "Clothes";
  List<String> clothes = [
    "Clothes",
    "Trousers",
    "T_Shirt",
    "Shirt",
    "Jacket",
    "dress",
    "skirt",
    
  ];
    var ocassion_type = "PersonType" ;
  String occasion = "Occasion";
  List<String> occasion_list = ["Occasion" ,"work" , "gradution" ,"wadding" ,"Sport" ,"Hinking_with_friends"];
  // String type = "PersonType" ;
  List<String> work_list = ["work" ,"officer" , "business" ,"engineer" ];
  List<String> gradution_list = ["gradution" ,"student" ];
   List<String> wadding_list = ["wadding" ,"relatives" ,"friend","brother" ];
   List<String> sport_list = ["Sport" ,"person" ];
   List<String> Hinking_list = ["Hinking_with_friends" ,"person" ];
  DropdownMenuItem<String> drop({required String value}) =>
      DropdownMenuItem<String>(
        value: value,
        child: Text(value),
      );
  var clothe_type = "type";
  String col = "Color";
  List<String> color = [
    "Color",
    "white",
    "offwite",
    "beige",
    "gold",
    "yellow",
    "hazal",
    "orange",
    "red",
    "vinous",
    "brown",
    "oil",
    "green",
    "cyan",
    "blue",
    "darkblue",
    "sumo",
    "pink",
    "purple",
    "silver",
    "gray",
    "black",
  ];
  List<String> chickList(String choise) {
    if (choise == "Trousers") {
      return type_trouser;
    }
    if (choise == "T_Shirt") {
      return type_Tshirt;
    }
    if (choise == "Shirt") {
      return type_Shirt;
    }
    if (choise == "Shoes") {
      return type_shose;
    }
    if (choise == "Coat") {
      return type_coat;
    }

    if (choise == "Hat") {
      return type_Hat;
    }
    if (choise == "carafe") {
      return type_corafee;
    }
    if (choise == "Jacket") {
      return type_jacket;
    }
    if (choise == "dress") {
      return type_dress;
    }

    if (choise == "skirt") {
      return type_skirt;
    }
    if (choise == "waistband") {
      return type_Waistband;
    }
    if (choise == "formal_suit") {
      return type_Formal_Suit;
    }
    if (choise == "graduation_gown") {
      return type_graduation_gown;
    }
    return [];
  }
   List<String> chickListt(String choise) {
   
    if (choise == "work") {
      return work_list;
    }
    if (choise == "gradution") {
      return gradution_list;
    }
    if (choise == "wadding") {
      return wadding_list;
    }
    if (choise == "Sport") {
      return sport_list;
    }

    if (choise == "Hinking_with_friends") {
      return Hinking_list;
    }
    return [];
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
         backgroundColor: Colors.amber,
        title:  defultButton(
                    func: () {
                     
                    },
                    size: 13,
                    text: "2. Coordinating clothes by occasion and one piece",
                    color: Colors.black,
                  ),
      ),
      backgroundColor: Colors.amber[50],
      body: Center(
        child: Container(
          child: Center(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                  Container(
                    color: Colors.amber,
                    child: Text(
            "Please Enter the occasion :",
            style: TextStyle(
              color: Colors.black,
              fontSize: 18,
              fontWeight: FontWeight.bold,
            ),
          ),
                  ),
                  SizedBox(
                    height: 10,
                  ),
                Padding(
                      padding: const EdgeInsets.all(10.0),
                      child: Container(
                        width: double.infinity,
                        decoration:
                            BoxDecoration(border: Border.all(color: Colors.black)),
                        child: Center(
                          child: DropdownButton<String>(
                            hint: Text("Occasion Name"),
                            value: occasion,
                            onChanged: (String? _newGrade) {
                              setState(
                                () {
                                  occasion = _newGrade!;
                                  ocassion_type = _newGrade;
                                },
                              );
                              // _changeGrade(_newGrade);
                            },
                            items: occasion_list.map<DropdownMenuItem<String>>(
                              (String value) {
                                return drop(value: value);
                              },
                            ).toList(),
                          ),
                        ),
                      ),
                    ),
                    SizedBox(
                    height: 10,
                  ),
                   Container(
                    
                    color: Colors.amber,
                    child: Text(
            "Please Enter the person's type for the occasion :",
            style: TextStyle(
              color: Colors.black,
              fontSize: 18,
              fontWeight: FontWeight.bold,
              
            ),
            maxLines: 2,
          ),
                  ),
                  SizedBox(
                    height: 10,
                  ),
                    Padding(
                      padding: const EdgeInsets.all(8.0),
                      child: Container(
                         width: double.infinity,
                        decoration:
                            BoxDecoration(border: Border.all(color: Colors.black)),
                        child: Center(
                          child: DropdownButton<String>(
                            hint: Text("Person Type"),
                            value: ocassion_type,
                            onChanged: (String? _newGrade) {
                              setState(
                                () {
                                  ocassion_type = _newGrade!;
                                },
                              );
                              // _changeGrade(_newGrade);
                            },
                            items: chickListt(occasion).map<DropdownMenuItem<String>>(
                              (String val) {
                                return drop(value: val);
                              },
                            ).toList(),
                          ),
                        ),
                      ),
                    ),
                SizedBox(
                    height: 10,
                  ),
                   Container(
                    
                    color: Colors.amber,
                    child: Text(
            "Please Enter the name , type and color Piece of clothes :",
            style: TextStyle(
              color: Colors.black,
              fontSize: 15,
              fontWeight: FontWeight.bold,
              
            ),
            maxLines: 2,
          ),
                  ),
                Padding(
                  padding: const EdgeInsets.all(8.0),
                  child: Container(
                    decoration:
                        BoxDecoration(border: Border.all(color: Colors.black)),
                    child: DropdownButton<String>(
                      hint: Text("Clothe Name"),
                      value: clothes_,
                      onChanged: (String? _newGrade) {
                        setState(
                          () {
                            clothes_ = _newGrade!;
                            clothe_type = _newGrade;
                          },
                        );
                        // _changeGrade(_newGrade);
                      },
                      items: clothes.map<DropdownMenuItem<String>>(
                        (String value) {
                          return drop(value: value);
                        },
                      ).toList(),
                    ),
                  ),
                ),
                Padding(
                  padding: const EdgeInsets.all(8.0),
                  child: Container(
                    decoration:
                        BoxDecoration(border: Border.all(color: Colors.black)),
                    child: DropdownButton<String>(
                      hint: Text("Clothe Color"),
                      value: col,
                      onChanged: (String? _newGrade) {
                        setState(
                          () {
                            col = _newGrade!;
                          },
                        );
                        // _changeGrade(_newGrade);
                      },
                      items: color.map<DropdownMenuItem<String>>(
                        (String value) {
                          return drop(value: value);
                        },
                      ).toList(),
                    ),
                  ),
                ),
                Padding(
                  padding: const EdgeInsets.all(8.0),
                  child: Container(
                    decoration:
                        BoxDecoration(border: Border.all(color: Colors.black)),
                    child: DropdownButton<String>(
                      hint: Text("Clothe Type"),
                      value: clothe_type,
                      onChanged: (String? _newGrade) {
                        setState(
                          () {
                            clothe_type = _newGrade!;
                          },
                        );
                        // _changeGrade(_newGrade);
                      },
                      items: chickList(clothes_).map<DropdownMenuItem<String>>(
                        (String val) {
                          return drop(value: val);
                        },
                      ).toList(),
                    ),
                  ),
                ),
                 Padding(
                  padding: const EdgeInsets.all(30.0),
                  child: GestureDetector(
                    child: Container(
                      height: 50,
                      width: 90,
                      decoration: BoxDecoration(
                        borderRadius: BorderRadius.circular(10),
                        color: Colors.black,
                      ),
                      child: Center(
                        child: Text(
                          'Done',
                          style: TextStyle(
                            fontWeight: FontWeight.bold,
                            color: Colors.white,
                            fontSize: 20,
                          ),
                        ),
                      ),
                    ),
                    onTap: () {
                      _SecondScreen(occasion , ocassion_type ,clothes_ , clothe_type , col ).then((value)
                      {
                        if (value = true)
                        {
                          _awaitReturnValueFromScreen(context);
                        }
                      }
                      );
                      
                    },
                  ),
                )
              ],
            ),
          )
        ),
      ),
    );
  }
   void _awaitReturnValueFromScreen(BuildContext context) async {

    // start the SecondScreen and wait for it to finish with a result
    final result = await Navigator.push(
        context,
        MaterialPageRoute(
          builder: (context)=>
            OutPutSecond()   
        ));
   }
    Future <bool> _SecondScreen (String occasion , String personType ,String clothe , String type , String color ,)
  async {
    Dio dio = Dio();
    final prefs = await SharedPreferences.getInstance();
    var userid = prefs.getString('USERID');
    Map<String , dynamic> map =
    {
      "USERID" : userid ,
      "Occasion" : occasion ,
      "PersonType" : personType ,
       "ClotheName" : clothe ,
      "Type" : type ,
      "Color" : color ,
    };
    var response = await dio.post(Url.SECOUNDSCREEN , data: map);
    if (response.data["Code"] == 200) 
    {
      return true ;
    }
    else return false;
  }
}