import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';
import 'package:login/modules/SelectionButton.dart';
import 'package:login/modules/first_screan/first_screen.dart';
import 'package:login/modules/homebage/Homebage.dart';
import 'package:login/modules/secound_screen/secound_screen.dart';
import 'package:login/modules/third_screen/third_scree.dart';
import 'package:login/shared/components/components.dart';

class choice extends StatefulWidget {
  const choice({Key? key}) : super(key: key);

  @override
  State<choice> createState() => _choiceState();
}

class _choiceState extends State<choice> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.amber[50],
      // appBar: AppBar(
      //   backgroundColor: Colors.amber,
      // ),
      body: Container(
        child: Center(
          child: Column(
            children: [
               SizedBox(
                height: 50,
              ),
              Expanded(
                child: Padding(
                  padding: const EdgeInsets.only(left: 30.0 ,right: 30 ,top: 30),
                  child: Container(
      
      decoration: BoxDecoration(
        borderRadius: BorderRadius.circular(20),
        color: Colors.amber,
  
      ),
      padding: const EdgeInsets.all(10),
        child: Center(
          child: Text(
            "Choose one of the following options :",
            style: TextStyle(
              color: Colors.black,
              fontSize: 18,
              fontWeight: FontWeight.bold,
            ),
          ),
        ),
    ),
                ),
              ),
    
              SizedBox(
                height: 10,
              ),
              Expanded(
                child: Center(
                  child: defultButton(
                    func: () {
                      _awaitReturnValueFirstScreen(context);
                    },
                    size: 15,
                    text: "1. Coordinating clothes by occasion only",
                    color: Colors.black,
                  ),
                ),
              ),
              SizedBox(
                height: 5.0,
              ),
              Center(
                child: defultButton(
                  func: () {
                    _awaitReturnValueSecoundScreen(context);
                  },
                  size: 13,
                  text: "2. Coordinating clothes by occasion and one piece",
                  color: Colors.black,
                ),
              ),
              SizedBox(
                height: 5.0,
              ),
              Expanded(
                child: Center(
                  child: defultButton(
                    func: () {
                      _awaitReturnValueThirdScreen(context);
                    },
                    size: 12.5,
                    text: "3. Coordinating clothes by occasion and piece image",
                    color: Colors.black,
                  ),
                ),
              ),

               Expanded(
                child: Center(
                  child: defultButton(
                    func: () {
                      _awaitReturnScreen(context);
                    },
                    size: 15,
                    text: "add clothes",
                    color: Colors.black,
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  void _awaitReturnValueFirstScreen(BuildContext context) async {
    // start the SecondScreen and wait for it to finish with a result
    final result = await Navigator.push(
        context, MaterialPageRoute(builder: (context) => FirstScreen()));
  }
   void _awaitReturnValueSecoundScreen(BuildContext context) async {
    // start the SecondScreen and wait for it to finish with a result
    final result = await Navigator.push(
        context, MaterialPageRoute(builder: (context) => SecoundScreen()));
  }
   void _awaitReturnValueThirdScreen(BuildContext context) async {
    // start the SecondScreen and wait for it to finish with a result
    final result = await Navigator.push(
        context, MaterialPageRoute(builder: (context) => ThirdScreen()));
  }
     void _awaitReturnScreen(BuildContext context) async {
    // start the SecondScreen and wait for it to finish with a result
    final result = await Navigator.push(
        context, MaterialPageRoute(builder: (context) => MyHomePage()));
  }
}
