import 'dart:io';

import 'package:dio/dio.dart';
import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'package:login/modules/homebage/Homebage.dart';
import 'package:animated_background/animated_background.dart';
import 'package:login/shared/components/components.dart';
import 'package:login/url.dart';
import 'package:shared_preferences/shared_preferences.dart';

class SelectinButton extends StatefulWidget {
  const SelectinButton({Key? key}) : super(key: key);

  @override
  State<SelectinButton> createState() => _SelectinButtonState();
}

class _SelectinButtonState extends State<SelectinButton>
    with TickerProviderStateMixin {
  String trouser = "Trousers";
  List<String> type_trouser = [
    "Trousers",
    "wide_pants",
    "jeans",
    "short",
    "pajama"
  ];
  String T_Shirt = "T_Shirt";
  List<String> type_Tshirt = ["T_Shirt", "Hoodie"];
  String Shirt = "Shirt";
  List<String> type_Shirt = ["Shirt"];
  String Skirt = "skirt";
  List<String> type_skirt = ["skirt", "jeans", "MidSkirt", "shortSkirt"];
  String shoes = "shose";
  List<String> type_shose = ["shose", "Kandra", "Sandal"];
  String Coat = "Coat";
  List<String> type_coat = ["Coat"];
  String Hat = "Hat";
  List<String> type_Hat = ["Hat"];
  String carafe = "carafe";
  List<String> type_corafee = ["carafe"];
  String Jacket = "Jacket";
  List<String> type_jacket = ["Jacket"];
  String dress = "dress";
  List<String> type_dress = ["dress", "Midriff", "Long_robe", "Mididress"];
  String waistband = "waistband";
  List<String> type_Waistband = ["waistband"];
  String formal_suit = "formal_suit";
  List<String> type_Formal_Suit = ["formal_suit", "formal_suit_skirt"];
  String graduation_gown = "graduation_gown";
  List<String> type_graduation_gown = ["graduation_gown"];
  String clothes_ = "Clothes";
  List<String> clothes = [
    "Clothes",
    "Trousers",
    "T_Shirt",
    "Shirt",
    "shose",
    "Coat",
    "Hat",
    "carafe",
    "Jacket",
    "dress",
    "skirt",
    "waistband",
    "formal_suit",
    "graduation_gown",
  ];
  String col = "Color";
  List<String> color = [
    "Color",
    "white",
    "beige",
    "gold",
    "yellow",
    "orange",
    "red",
    "vinous",
    "brown",
    "oil",
    "green",
    "cyan",
    "blue",
    "darkblue",
    "pink",
    "gray",
    "black",
  ];
  List<String> a = ["null", "null", "null", "null"];
  String str = "";
  String season = "";
  DropdownMenuItem<String> drop({required String value}) =>
      DropdownMenuItem<String>(
        value: value,
        child: Text(value),
      );
 

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
    if (choise == "shose") {
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

  var clothe_type = "type";

  final imagePicker = ImagePicker();
  File? imageFile;
  String camera = "null";
  var image;
  String valueSeasons = "summer";
  List<String> listSeasons = ["summer", "Spring", "Autumn", "winter"];

  Future getImageGallery() async {
    image = await imagePicker.getImage(source: ImageSource.gallery);
    setState(() {
      if ( image != null) 
      {
      imageFile = File(image!.path);
      camera = image.path;
      }
    
      print("pathhhhhhhh $camera");
    });
    Navigator.of(context).pop(imageFile);
  }

  Future getImageCamera() async {
    var image = await imagePicker.getImage(source: ImageSource.camera);
    setState(() {
      if (image != null)
    {
      imageFile = File(image.path);
      camera = image.path;
    }
     
      print("pathhhhhhhhhh $camera");
    });
    Navigator.of(context).pop(imageFile);
  }

  Future _showDialog() {
    return showDialog(
        context: context,
        builder: (context) => AlertDialog(
              actions: [
                Center(
                  child: Row(
                    children: [
                     
                        
                         Container(
                          
                          child: defultButton(text: "Gallery", func: (){
                            getImageGallery();
                          },
                          color: Colors.black)
                          ),
                      
                      Padding(
                        padding: const EdgeInsets.all(20.0),
                        child:  defultButton(text: "Camera", func:(){
                            getImageCamera();
                          },
                          color: Colors.black )
                        
                        
                      ),
                    ],
                  ),
                )
              ],
            ));
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Enter your clothes specifications'),
        backgroundColor: Colors.amber,
      ),
      body: Stack(
        children: [
          Container(
            color: Colors.amber[50],
            child: AnimatedBackground(
              behaviour: RandomParticleBehaviour(
                options: ParticleOptions(
                  spawnMaxRadius: 50,
                  spawnMinSpeed: 10.00,
                  particleCount: 68,
                  spawnMaxSpeed: 50,
                  minOpacity: 0.3,
                  spawnOpacity: 0.4,
                  //  baseColor: Colors.green,

                  image: Image(image: AssetImage('images/${valueSeasons}.png')),
                ),
              ),
              vsync: this,
              child: Center(
                child: Text(""),
              ),
            ),
          ),
          Center(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Container(
                    child: viewlist(
                  listSeasons: listSeasons,
                  set_State: (newValue) {
                    setState(() {
                      valueSeasons = newValue;

                      print(valueSeasons);
                    });
                  },
                  valueSeasons: valueSeasons,
                )
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
                  padding: const EdgeInsets.all(8.0),
                  child: Container(
                    decoration:
                        BoxDecoration(border: Border.all(color: Colors.black)),
                    child: MaterialButton(
                      onPressed: () {
                        _showDialog();
                      },
                      child: Text("Image"),
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
                      _selectionButton(clothes_,clothe_type , col, valueSeasons, imageFile!).then((value)
                      {
                        print('ssdsdsd');
                        if (value = true)
                        {
                          _sendDataBack(context);
                        }
                      }
                      );
                      
                    },
                  ),
                )
              ],
            ),
          ),
        ],
      ),
    );
  }

  void _sendDataBack(BuildContext context) {
    a.addAll([clothes_, clothe_type, col, camera, valueSeasons]);
    // a.add(col);
    print(a.length);
    str = "Season is : " +
        a[a.length - 1] +
        "\n"
            "Name clothe is : " +
        a[a.length - 5] +
        "\n" +
        "Type clothe is : " +
        a[a.length - 4] +
        "\n" +
        "Color clothe is : " +
        a[a.length - 3] +
        "\n" +
        "Path image is : " +
        a[a.length - 2] +
        "\n";

    Navigator.pop(context, str);
  }
  Future <bool> _selectionButton (String clothe , String type , String color , String season , File image)
  async {
    Dio dio = Dio();
    final prefs = await SharedPreferences.getInstance();
    var userid = prefs.getString('USERID');
    print('user iddddddddddddd $userid');
    // Map<String , dynamic> map =
    // {
    //   "USERID" : userid ,
    //   "Season" : season ,
    //   "ClotheName" : clothe ,
    //   "Type" : type ,
    //   "Color" : color ,
    //   // "Image" : image 
    // };
    FormData formData =FormData.fromMap({
       "USERID" : userid ,
      "Season" : season ,
      "ClotheName" : clothe ,
      "Type" : type ,
      "Color" : color ,
      "Image": await MultipartFile.fromFile(image.path)
    });
    // formData.files.add(value)['Image'] = await MultipartFile.fromFile(image.path);
    var response = await dio.post(Url.HOMEPAGE , data: formData,);
    print(response.data);
    if (response.data["Code"] == 200) 
    {
      return true ;
    }
    else return false ;
  }
 }
