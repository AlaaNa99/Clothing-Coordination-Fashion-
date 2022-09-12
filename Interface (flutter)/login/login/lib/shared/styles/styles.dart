// import 'dart:async';
// import 'dart:math';

// import 'package:flutter/cupertino.dart';
// import 'package:flutter/material.dart';
// import 'package:flutter_speed_dial/flutter_speed_dial.dart';
// import 'package:login/modules/SelectionButton.dart';
// import 'package:login/shared/components/components.dart';

// class MedPage extends StatefulWidget {
//   @override
//   _MedPageState createState() => _MedPageState();
// }

// class _MedPageState extends State<MedPage> {
//   List<String> items = [];
//   List<String> a = [];
//   String text = 'Text';
//   @override
//   Widget build(BuildContext context) {
//     return Scaffold(
//       appBar: AppBar(
//         title: Text('My med app'),
//       ),
//       body: Center(
//         child: Column(
//           mainAxisAlignment: MainAxisAlignment.spaceBetween,
//           crossAxisAlignment: CrossAxisAlignment.stretch,
//           children: <Widget>[
//             Expanded(
//               child: ListView.builder(
//                 itemBuilder: (context, index) {
//                   return ReusableListItem(Color(0xFFd2fddf), items[index]);
//                 },
//                 itemCount: items.length,
                
//               ),
//             )
            
//           ],
//         ),
//       ),
//       floatingActionButton: FloatingActionButton.extended(
//         icon: Icon(Icons.add),
//         label: Text("Add New Clothes "),
//        onPressed: () {
//                 _awaitReturnValueFromInformScreen(context);
//               },
//       ),
//     );
    
//   }
   

//     void _awaitReturnValueFromInformScreen(BuildContext context) async {

//     // start the SecondScreen and wait for it to finish with a result
//     final result = await Navigator.push(
//         context,
//         MaterialPageRoute(
//           builder: (context) => SelectinButton(),
//         ));

//     // after the SecondScreen result comes back update the Text widget with it
//     setState(() {
//       text = result;
//       items.add(text);
//       print(text);
//     });
//   }
  
   

// }

// class ReusableListItem extends StatelessWidget {
//   ReusableListItem(this.colour, this.pill);

//   final Color colour;
//   final String pill;
//   // final String coll;

//   @override
//   Widget build(BuildContext context) {
//     return Container(
//       height: 50,
//       margin: const EdgeInsets.all(8),
//       decoration: BoxDecoration(
//           color: colour, borderRadius: BorderRadius.circular(40.0)),
//       child: SingleChildScrollView(
//         child: Center(
//             child: Column(
//           children: [
//             Center(
//               child: Text(
//                 pill,
//               style: TextStyle(
//                 fontWeight: FontWeight.bold
//               ),),
//             ),
          
//           ],
//         )),
//       ),
//     );
//   }
 
// }
