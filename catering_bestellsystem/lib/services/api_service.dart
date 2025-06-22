import 'dart:convert';
import 'package:http/http.dart' as http;
import '../config.dart';

class ApiService {
  static Future<void> sendTestMessage(String text) async {
    final url = Uri.parse('${AppConfig.serverUrl}/message');
    try {
      final response = await http.post(
        url,
        headers: {'Content-Type': 'application/json'},
        body: json.encode({'text': text}),
      );
      print('Antwort vom Server: ${response.body}');
    } catch (e) {
      print('Fehler beim Senden: $e');
    }
  }
}
