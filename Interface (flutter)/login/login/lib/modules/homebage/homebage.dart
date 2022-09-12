import 'package:animated_background/animated_background.dart';
import 'package:login/modules/choice/choice.dart';
import 'package:login/modules/choice/choice.dart';
import 'package:login/shared/components/components.dart';
import 'package:login/modules/SelectionButton.dart';
import 'package:flutter/material.dart';

class MyHomePage extends StatefulWidget {
  const MyHomePage({Key? key}) : super(key: key);

  

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> with TickerProviderStateMixin {

  List<String> items = [];
  List<String> a = ["null" , "null" , "null" ,"null"];
  String text = 'Text';
  

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.amber,
        title:   
           Center(
             child: Row(
              children :[
                Expanded(
                  child: Text(
                  "Your Clothes",
                  style: TextStyle(
                    color: Colors.black,
                    fontWeight: FontWeight.bold ,
                    fontSize: 20
                  ),
                      
                    ),
                ),
                Padding(
                    padding: const EdgeInsets.only( left :10.0),
                    child: Expanded(
                       child: defultButton(text: 'Finish',
                        func: (){ _awaitReturnValueFromScreen(context);} )
                      // GestureDetector(
                      //   child: Container(
                      //     height: 40,
                      //     width: 90,
                      //     decoration: BoxDecoration(
                      //       borderRadius: BorderRadius.circular(20),
                      //       color: Colors.black,
                      //     ),
                      //     child: Center(
                      //       child: Text(
                      //         'Finish',
                      //         style: TextStyle(
                      //           fontWeight: FontWeight.bold,
                      //           color: Colors.white,
                      //           fontSize: 20,
                      //         ),
                      //       ),
                      //     ),
                      //   ),
                      //   onTap: () {
                      //     _awaitReturnValueFromScreen(context);
                      //   },
                      // ),
                    ),
                  )
              ]
                ),
           ),
          
      ),
      body:
       Container(
        color: Colors.amber[50],
         child: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: <Widget>[
              Expanded(
                child: ListView.builder(
                  itemBuilder: (context, index) {
                    return ReusableListItem(Colors.black12, items[index]);
                  },
                  itemCount: items.length,
                  
                ),
              ),
              
            ],
          ),
      ),
       ),

        
      
       floatingActionButton: FloatingActionButton.extended(
        backgroundColor: Colors.black,
        icon: Icon(Icons.add),
        label: Text("Add New Clothes "),
       onPressed: () {
                _awaitReturnValueFromInformScreen(context);
              },
      ),
    );
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
            SelectinButton()   
        ));

    // after the SecondScreen result comes back update the Text widget with it
    setState(() {
      text = result;
      items.add(text);
      print(text);
    });
  }
 

    // after the SecondScreen result comes back update the Text widget with it
    
  }
  

class ReusableListItem extends StatelessWidget {
  ReusableListItem(this.colour, this.pill);

  final Color colour;
  final String pill;
  // final String coll;

  @override
  Widget build(BuildContext context) {
    return Container(
      height: 70,
      margin: const EdgeInsets.all(8),
      decoration: BoxDecoration(
      color: colour, borderRadius: BorderRadius.circular(30.0)),
      child: SingleChildScrollView(
        child: Center(
            child: Column(
          children: [
            Center(
              child: Padding(
                padding: const EdgeInsets.all(8.0),
                child: Text(
                  pill,
                style: TextStyle(
                  fontWeight: FontWeight.bold
                ),),
              ),
            ),
          
          ],
        )),
      ),
    );
  }
 
}