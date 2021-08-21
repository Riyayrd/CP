bool find_sum_of_two(vector<int>& A, int val) {
  unordered_set<int> found_values;
  for (int& a : A) {
    if (found_values.find(val - a) != found_values.end()) {
      return true;
    }
    found_values.insert(a);
  }
  return false;
}

int main() {
  vector<int> v = {5, 7, 1, 2, 8, 4, 3};
  vector<int> test = {3, 20, 1, 2, 7};

  for(int i=0; i<test.size(); i++){
    bool output = find_sum_of_two(v, test[i]);
    cout << "find_sum_of_two(v, " << test[i] << ") = " << (output ? "true" : "false") << endl;
  }
  return 0;
}
