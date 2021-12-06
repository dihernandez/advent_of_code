#include <string>
#include <fstream>
#include <vector>
#include <iostream>

std::vector<int> get_input() {
    std::fstream input_file("sonar_sweep_input.txt");
   std::string line_str;
   std::vector<int> input_vec;
   if (input_file.is_open()) {
       while(getline(input_file, line_str)) {
           input_vec.push_back(std::stoi(line_str));        
    }
       input_file.close();
   }
   return input_vec;
}

int part_1(std::vector<int> input_vec) {
    int num_increases = 0;

    for(int i = 1; i < input_vec.size(); i++) {
        if(input_vec.at(i - 1) < input_vec.at(i)) {
                num_increases++;
        }
    }
    return num_increases;
}

int part_2(std::vector<int> input_vec){
    std::vector<int> summed_triplets;
    for(int i = 2; i < input_vec.size(); i++){
        summed_triplets.push_back(input_vec.at(i - 2) + input_vec.at(i - 1) + input_vec.at(i));
    }
    return part_1(summed_triplets);
}

int main(){
    int solution_1 = part_1(get_input());
    std::cout << "solution part 1 is " << solution_1 << std::endl;
    int solution_2 = part_2(get_input());
    std::cout << "solution part 2 is " << solution_2 << std::endl; 
    return 0;
}
