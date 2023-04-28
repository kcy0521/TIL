import 'dart:convert';

import 'package:http/http.dart' as http;
import 'package:webtoon/models/webtoon.dart';

class ApiService {
  static const String baseUrl =
      "https://webtoon-crawler.nomadcoders.workers.dev";
  static const String today = "today";

  static Future<List<WebtoonModel>> getTodaysToons() async {
    List<WebtoonModel> webtoonInstances = [];
    final url = Uri.parse('$baseUrl/$today');
    final response = await http.get(url);
    // 응답을 받을때까지 기다리게 해야한다.
    if (response.statusCode == 200) {
      // final List<dynamic> webtoons = jsonDecode(response.body);
      final webtoons = jsonDecode(response.body);
      for (var webtoon in webtoons) {
        webtoonInstances.add(WebtoonModel.fromJson(webtoon));
        // #6.4 Recap -> 4:50 부터 강의 들으면 나옴
      }
      return webtoonInstances;
    }
    throw Error();
  }
}
