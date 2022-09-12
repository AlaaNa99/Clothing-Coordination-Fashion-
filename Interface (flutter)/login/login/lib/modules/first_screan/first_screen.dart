import 'package:dio/dio.dart';
import 'package:flutter/material.dart';
import 'package:login/modules/output/output.dart';
import 'package:login/shared/components/components.dart';
import 'package:login/url.dart';
import 'package:shared_preferences/shared_preferences.dart';

class FirstScreen extends StatefulWidget {
  const FirstScreen({ Key? key }) : super(key: key);

  @override
  State<FirstScreen> createState() => _FirstScreenState();
}

class _FirstScreenState extends State<FirstScreen> {
   DropdownMenuItem<String> drop({required String value}) =>
      DropdownMenuItem<String>(
        value: value,
        child: Text(value),
      );
  var ocassion_type = "PersonType" ;
  String occasion = "Occasion";
  List<String> occasion_list = ["Occasion" ,"work" , "gradution" ,"wadding" ,"Sport" ,"Hinking_with_friends"];
  // String type = "PersonType" ;
  List<String> work_list = ["work" ,"officer" , "business" ,"engineer" ];
  List<String> gradution_list = ["gradution" ,"student" ];
   List<String> wadding_list = ["wadding" ,"relatives" ,"friend","brother" ];
   List<String> sport_list = ["Sport" ,"person" ];
   List<String> Hinking_list = ["Hinking_with_friends" ,"person" ];
    List<String> chickList(String choise) {
   
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
        title: defultButton(
                    func: () {
                      
                    },
                    size: 15,
                    text: "1. Coordinating clothes by occasion only",
                    color: Colors.black,
                  ),),
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
                            items: chickList(occasion).map<DropdownMenuItem<String>>(
                              (String val) {
                                return drop(value: val);
                              },
                            ).toList(),
                          ),
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
                      _FirstScreen(occasion , ocassion_type).then((value)
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
          ),
        ),
      )
      ,
    );
  }
      void _awaitReturnValueFromScreen(BuildContext context) async {

    // start the SecondScreen and wait for it to finish with a result
    final result = await Navigator.push(
        context,
        MaterialPageRoute(
          builder: (context)=>
            OutPut()   
        ));
   }
    Future <bool> _FirstScreen (String occasion , String personType)
  async {
    Dio dio = Dio();
    final prefs = await SharedPreferences.getInstance();
    var userid = prefs.getString('USERID');
    Map<String , dynamic> map =
    {
      "USERID" : userid ,
      "Occasion" : occasion ,
      "PersonType" : personType ,
      
    };
    var response = await dio.post(Url.FIRSTSCREEN , data: map);
    if (response.data["Code"] == 200) 
    {
      return true ;
    }
    else return false;
  }
}