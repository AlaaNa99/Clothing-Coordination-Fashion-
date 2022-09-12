import 'package:dio/dio.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:login/modules/SelectionButton.dart';
import 'package:login/modules/choice/choice.dart';
import 'package:login/modules/login/signin.dart';
import 'package:login/modules/secound_screen/secound_screen.dart';
import 'package:login/shared/components/components.dart';
import 'package:login/url.dart';
import 'package:shared_preferences/shared_preferences.dart';

class LogIn extends StatefulWidget {
  @override
  State<LogIn> createState() => _LogInState();
}

class _LogInState extends State<LogIn> {
  var emailController =  TextEditingController() ;
  bool isLoading = false;

  var passController =  TextEditingController() ;

  var fromKey  = GlobalKey <FormState>() ;

  bool isPassword = true ;

  Widget build(BuildContext context) {
    return  Container(
             width: MediaQuery.of(context).size.width,
   height: MediaQuery.of(context).size.height,
            decoration: BoxDecoration(
            image: DecorationImage(
              image:AssetImage(
                    "images/login.PNG"),
              fit: BoxFit.cover,
              // color: Colors.white.withOpacity(.9),
              // colorBlendMode: BlendMode.modulate,
    
            ),),
          child :
    
     Scaffold(
       backgroundColor: Colors.transparent,
    appBar: AppBar(
    //  title:   Padding(
    //     padding: const EdgeInsets.only(right: 10, left :100 ,top: 30 ,bottom: 20),
    //     child:
    //   ),
     
       backgroundColor: Colors.transparent,
        elevation: 0.0,
      ),
      extendBodyBehindAppBar: true,
      // لحتى ماتتحرك
      // resizeToAvoidBottomInset: false,
      body:
       Stack(
        children: [
          // Container(
          //   width: double.infinity,
          //   height: double.infinity,
          //   child: Image(
          //     image:AssetImage(
          //           "images/login.PNG"),
          //     fit: BoxFit.cover,
          //     color: Colors.white.withROpacity(.9),
          //     colorBlendMode: BlendMode.modulate,
    
          //   ),
          // ),
          Padding(
            padding: const EdgeInsets.only(left: 140, top: 100, right: 20),
            child: SingleChildScrollView(
               child: Form(
                 key: fromKey,
                 child: Column(
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
                    height: 50.0,
                  ),
                  Text(
                    'User Login',
                    style: TextStyle(fontSize: 20,
                    fontWeight: FontWeight.bold
                    ),
                  ),
                  SizedBox(
                    height: 40,
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
                          
                        }),
                  SizedBox(
                    height: 40.0,
                  ),
                 defultButton (
                   func:  ()  {
                     if (fromKey.currentState!.validate()){
                      // _awaitReturnValueFromScreen(context);
                     print (emailController.text);
                     print(passController.text) ;
                    //  setState(() {
                    //    isLoading = true;
                    //  });
                      _login(emailController.text, passController.text).then((value) async {

                      if (value)
                      {
                        // final prefs = await SharedPreferences.getInstance();
                        
                        _awaitReturnValueFromScreen(context);
                      }
                     });
                     
                     }
                    
                      
                     
                    },
                    text:"login",
                    color: Colors.black ,
                      
                 ),
                  SizedBox(
                    height: 40.0,
                  ),
                
                  Row(
                    children: [
                      Expanded(
                        child: Text(
                          'Don\'t have an acount ?',
                          maxLines: 1,
                          style: TextStyle(
                            fontWeight: FontWeight.bold,
                            fontSize: 11,
                          ),),
                      ),
                      Expanded(
                        child: TextButton(onPressed: (){
                        _awaitReturnValueFromInformScreen(context);
                        },
                         child: Text (
                          //  MediaQuery.of(context).size.height
                           'Sign Up'
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
    ));
  }
     void _awaitReturnValueFromScreen(BuildContext context) async {

    // start the SecondScreen and wait for it to finish with a result
    final result = await Navigator.push(
        context,
        MaterialPageRoute(
          builder: (context)=>
            choice()   
        ));
   }
   void _awaitReturnValueFromInformScreen(BuildContext context) async {

    // start the SecondScreen and wait for it to finish with a result
    final result = await Navigator.push(
        context,
        MaterialPageRoute(
          builder: (context)=>
            SignIn()   
        ));

    // after the SecondScreen result comes back update the Text widget with it
    
  }
  Future<bool> _login( String username, String password ) async {
    Dio dio =Dio();
    Map<String,dynamic> map ={
      "Username" : username,
    "Password" : password
    };
    
    var response = await dio.post(Url.LOGIN,data: map);
    
    if (response.data["Code"] == 200)
    {
       final prefs = await SharedPreferences.getInstance();
       await prefs.setString('userId', response.data['USERID']);
      return true;
    }
    else return false;
  
  }
}
