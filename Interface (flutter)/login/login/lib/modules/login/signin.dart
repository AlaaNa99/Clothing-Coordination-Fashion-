import 'package:dio/dio.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:login/modules/choice/choice.dart';
import 'package:login/modules/choice/choice.dart';
import 'package:login/modules/homebage/homebage.dart';
import 'package:login/modules/secound_screen/secound_screen.dart';
import 'package:login/shared/components/components.dart';
import 'package:login/url.dart';
import 'package:shared_preferences/shared_preferences.dart';

import 'login.dart';

class SignIn extends StatefulWidget {
  @override
  State<SignIn> createState() => _SignInState();
}

class _SignInState extends State<SignIn> {
  var emailController =  TextEditingController() ;
  var passController =  TextEditingController() ;
  var ageControler = TextEditingController();
  var skinColorController = TextEditingController();
  var genderControler = TextEditingController();

  var fromKey  = GlobalKey <FormState>() ;

  bool isPassword = true ;

   String gender = " Gender" ;
  List <String> gender_list = [" Gender",  "male" , "female"];
  String sk_color = "SkinColor" ;
  List <String> skColor_list = ["SkinColor" , "white" ,"dark" ,"hanatawi"];
   String age = "  Age" ;
  List <String> age_list = ["  Age" ,"15","16","17","18","19","20","21","22","23","24","25","26",
  "27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44",
  "45","46","47","48","49","50","51","52","53","54","55","56","57","58","59"];
  Widget build(BuildContext context) {
    return Scaffold(
    appBar: AppBar(
   
     
       backgroundColor: Colors.transparent,
        elevation: 0.0,
      ),
      extendBodyBehindAppBar: true,
      body:
       Stack(
        children: [
          Container(
            width: double.infinity,
            height: double.infinity,
            child: Image(
              image:AssetImage(
                    "images/login.PNG"),
              fit: BoxFit.cover,
              color: Colors.white.withOpacity(.9),
              colorBlendMode: BlendMode.modulate,
            ),
          ),
         
             SingleChildScrollView(
               child: Form(
                 key: fromKey,
                 child:
                  Padding(
            padding: const EdgeInsets.only(left: 140, top: 100,right: 20),
            child :
                  Column(
              children: [
                 Text(
                      'Clothes\nCoordination',
                      maxLines: 2,
                      textAlign: TextAlign.center,
                      style: TextStyle(
                        fontSize: 26.0,
                        color: Colors.black,
                        fontWeight: FontWeight.bold,
                      ),
        ),
                 
                  SizedBox(
                    height: 40.0,
                  ),
                 
                  Text(
                    'User Sign Up',
                    style: TextStyle(fontSize: 20,
                    fontWeight: FontWeight.bold
                    ),
                  ),
                  SizedBox(
                    height: 30,
                  ),
                  // Email
                  defultFormField(
                  controller: emailController,
                   type: TextInputType.emailAddress, 
                   hintText: 'Email Address',
                    prefix: Icons.email, 
                     onChange: (value)
                     {
                       print(value);
                     },
                      validate: ( value)
                      {
                        if ( value!.isEmpty)
                        {
                          print('alaa');
                          return 'email address is not be empty' ;
                        }
                        return null ;
                      }),
                  SizedBox(
                    height: 20,
                  ),
                  // Password
                    defultFormField(
                    controller: passController,
                     type:TextInputType.visiblePassword ,
                      hintText: 'Password', 
                      prefix: Icons.lock,
                       sufix:isPassword ? Icons.visibility_off : Icons.visibility , 
                       onChange:(val){ print(val);},
                       isPassword: isPassword,
                       sufixpressed: (){
                         setState(() {
                           isPassword = !isPassword;
                         });
                        } ,
                      validate: ( value)
                        {
                          if (value!.isEmpty)
                          {
                            return 'password must be not empty';
                          }
                          
                        }
                        
                        ),
                         SizedBox(
                    height: 20,
                  ), 
                  Row(
                    children: [
                     
                              viewlist(
                              listSeasons: gender_list,
                              set_State: (newValue){
                                  setState(() {
                                  gender = newValue ;
                                    });
                                    },
                                valueSeasons: gender ,    
                ),
                SizedBox(
                    width: 20.0,
                  ),
                      viewlist(
                              listSeasons: age_list,
                              set_State: (newValue){
                                  setState(() {
                                  age = newValue ;
                                    });
                                    },
                                valueSeasons: age ,    
                                
                ),
                   
                  
                    ],
                  ),
                       viewlist(
                              listSeasons: skColor_list,
                              set_State: (newValue){
                                  setState(() {
                                  sk_color = newValue ;
                                    });
                                    },
                                valueSeasons: sk_color ,    
                                
                ),    
                  SizedBox(
                    height: 40.0,
                  ),
                 defultButton (
                   func:  (){
                     if (fromKey.currentState!.validate()){
                      // _awaitReturnValueFromScreen(context);
                     print (emailController.text);
                     print(passController.text) ;
                    _signin(emailController.text, passController.text, age, sk_color, gender).then((value) {
                      if (value == true) 
                      {
                        _awaitReturnValueFromScreen(context);
                      }
                    });
                     }
                     
                    },
                    text:"Sign Up",
                    color: Colors.black ,
                      
                 ),
                  SizedBox(
                    height: 20.0,
                  ),
                
                  Row(
                    children: [
                      Expanded(
                        child: Text(
                          'Do you have an acount ?',
                          maxLines: 1,
                          style: TextStyle(
                            fontSize: 10,
                            fontWeight: FontWeight.bold
                          ),),
                      ),
                      Expanded(
                        child: TextButton(onPressed: (){
                            _awaitReturnValueLogInScreen(context);
                        },
                         child: Text (
                          
                           'LogIn'
                         ),
                         ),
                      ),
                    ],
                  ), 
                  
              ],
            ),
               ), 
             
            ),
            
          ),
        ],
      ),
    );
  }
       void _awaitReturnValueFromScreen(BuildContext context) async {

    // start the SecondScreen and wait for it to finish with a result
    final result = await Navigator.push(
        context,
        MaterialPageRoute(
          builder: (context)=>
            MyHomePage()   
        ));
   }

        void _awaitReturnValueLogInScreen(BuildContext context) async {

    // start the SecondScreen and wait for it to finish with a result
    final result = await Navigator.push(
        context,
        MaterialPageRoute(
          builder: (context)=>
            LogIn()   
        ));
   }
   Future <bool> _signin (String username , String password ,String age , String skColor , String gender)
   async {
    Dio dio = Dio() ;
   
    Map<String , dynamic> map =  {
      // "USERID" : userid,
      "Username" : username ,
      "Password" : password ,
      "Age" : age ,
      "SkinColor" :sk_color ,
      "Gender" :gender  
    };
    print(map);
    var response =await dio.post(Url.SIGNUP, data: map);
    print(response);
     final prefs = await SharedPreferences.getInstance();
    var userid = prefs.setString('USERID',response.data['USERID']);
    if (response.data["Code"] == 200)
    return true ;
    else 
    return false ;
   } 

}
