import 'package:dio/dio.dart';
import 'package:flutter/material.dart';
import 'package:login/modules/choice/choice.dart';
import 'package:login/modules/homebage/homebage.dart';
import 'package:login/shared/components/components.dart';
import 'package:login/url.dart';
import 'package:shared_preferences/shared_preferences.dart';

class OutPut extends StatefulWidget {
  const OutPut({Key? key}) : super(key: key);

  @override
  State<OutPut> createState() => _OutPutState();
}

class _OutPutState extends State<OutPut> with SingleTickerProviderStateMixin {
  // late AnimationController _controller;

  // @override
  // void initState() {
  //   super.initState();
  //   _controller = AnimationController(vsync: this);
  // }
List<Widget> listImage = [];
bool b = false ;
  @override
  void dispose() {
    // _controller.dispose();
   listImage = [];
    super.dispose();
  }
  
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.amber,
        actions: [ Expanded(
                child: Center(
                  child: defultButton(
                    func: () {
                      listImage = [];
                      _awaitReturnScreen(context);
                    },
                    size: 15,
                    text: "done",
                    color: Colors.black,
                  ),
                ),
              ),],
        // title: Text(""),
      ),
      body: Container(
        height: MediaQuery.of(context).size.height,
        color: Colors.amber[50],
        child: FutureBuilder(
            future: getData(),
            builder: (context, AsyncSnapshot snapshot) {
              if (snapshot.connectionState == ConnectionState.waiting) {
                
                Center(child: CircularProgressIndicator(color: Colors.black));
              } else if (snapshot.hasData) {
                listImage = [];
                List<String> listOfKeys =snapshot.data.keys.toList();
                listOfKeys.removeAt(0); 
                print(listOfKeys);
                print('kkkkkkkkkkkk');
                
                listOfKeys.forEach((element) {
                  listImage.add(Center(
                    child: Text(element),
                    
                  ));
                  
                  for (int i = 0; i <  snapshot.data[element].length; i++) {
                    
                    print(snapshot.data[element][i]);
                    listImage.add(imageBuilder(snapshot.data[element][i]));
                  }
          
                });
                return ListView(
                  children:listImage,
                  
                );
              
                // return ListView.builder(
                //     key: GlobalKey(),
                //     shrinkWrap: true,
                //     itemCount: snapshot.data['image1'].length,
                //     itemBuilder: (context, index) {
                //       return imageBuilder(snapshot.data['image1'][index]);
                //     });
              } else if (snapshot.hasError) {
                return Center(
                  child: Row(
                    children: [Text('Error with get data'), Icon(Icons.flag)],
                  ),
                );
              }
              return Container();
            }),
      ),
    );
  }

  Future<dynamic> getData() async {
    Dio dio = Dio();
    final prefs = await SharedPreferences.getInstance();
    String userid = prefs.getString('USERID')!;
    var response =
        await dio.get(Url.OUTPUTFIRST + '?USERID=$userid');

    return response.data;
  }

  Widget imageBuilder(String url) {
    return SizedBox(height: MediaQuery.of(context).size.height/4,child: Image.network('${Url.URL}/$url'));
  }

       void _awaitReturnScreen(BuildContext context) async {
    // start the SecondScreen and wait for it to finish with a result
    final result = await Navigator.push(
        context, MaterialPageRoute(builder: (context) => choice()));
  }

}
