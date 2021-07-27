import csv

class SchoolTest:

    def __init__(self, file_name:str):        

        self.file_name = file_name
        self.dis_school_name = {}
        self.dis_school_name = {}
         
    def read_csv(self):

        with open(self.file_name, encoding='cp1252') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:

                if line_count == 0:
                    line_count += 1
                else:
                    self.dis_school_name[row[3]] = {'NCESSCH':row[0], 
                                                    'LEAID':row[1], 
                                                    'LEANM05':row[2], 
                                                    'school':row[3], 
                                                    'city':row[4], 
                                                    'state':row[5],
                                                    'LATCOD':row[6],
                                                    'LONCOD':row[7],
                                                    'MLOCALE':row[8],
                                                    'ULOCALE':row[9],
                                                    'status':row[10],
                                                    }

                    line_count += 1
                    
        return self

    def get_total_school(self):
                
        """
        Get total number of distinct school..
        """

        return (len(self.dis_school_name))
            
    def get_total_school_state_wise(self):
        
        """
        Get number of school which is belong to given state..
        """
        state_dic = {}

        for key, value in self.dis_school_name.items():

            if value['state'] in state_dic.keys(): 
                state_dic[value['state']] += 1
            else:
                state_dic[value['state']] = 1
 
        return state_dic

    def get_largest_school_in_city(self):
        
        """
        Get larget scholl in city..
        """ 
        city_dic = {}
        for key, value in self.dis_school_name.items():
             
            if value['city'] in city_dic.keys(): 
                city_dic[value['city']] += 1
            else:
                city_dic[value['city']] = 1
 
        max_city_name = max(city_dic, key=city_dic.get) 
        return max_city_name, city_dic[max_city_name]

    def get_metro_centric_locale(self):
        
        """
        Get number of schools are in each Metro-centric locale
        """ 
        metro_dic = {}
        for key, value in self.dis_school_name.items():
             
            try:
                if value['city'] in metro_dic.keys():
                    metro_dic[value['city']] += int(value['MLOCALE'])
                else:
                    metro_dic[value['city']] = int(value['MLOCALE'])
            except:
                pass
        return metro_dic

      
    def get_min_one_school_in_city(self):
        
        """
        Get min one school in a city..
        """ 
        city_dic = {}
        for key, value in self.dis_school_name.items():
             
            if value['city'] in city_dic.keys(): 
                city_dic[value['city']] += 1
            else:
                city_dic[value['city']] = 1
  
        return city_dic

      
    def search_by_value(self, search_key:str):
        
        """
        search based on key..
        """ 
        primary_search_list = []
        secondary_search_list = []
        for key, value in self.dis_school_name.items():
             
            
            if search_key == key or search_key == value['state'] or search_key == value['city']: 
                primary_search_list.append(value)                                                                                                                                                                                                                                                                                                                                                     
            elif search_key in key or search_key in value['state'] or search_key in value['city']:
                secondary_search_list.append(value)                                                                                                                                                                                                                                                                                                                                                    
  
        primary_search_list.extend(secondary_search_list)

        return primary_search_list


if __name__ ==  '__main__':

    obj = SchoolTest('school_test.csv')
    obj.read_csv()

    question_no = 1
   
    if question_no == 1:
        #QUES(1):- How many total schools are in this data set? 
        print('Total Schools:',obj.get_total_school())

    elif question_no == 2:

        #QUES(2):- How many schools are in each state?
        print('Schools by State:')
        for key ,value in obj.get_total_school_state_wise().items():
            print(key, ':', value)

    elif question_no == 3:
        #QUES(3):- How many schools are in each Metro-centric locale?
        for key,value in obj.get_metro_centric_locale().items():
            print(f'{key}:{value}')

    elif question_no == 4:
        #QUES(4):- Which city has the most schools? How many?
        city, num_of_school = obj.get_largest_school_in_city()
        print(f'city {city} have {num_of_school} schools.')

    elif question_no == 5:
        #QUES(5):- How many unique cities have at least one school in it? Which are they??
        city_name = obj.get_min_one_school_in_city()
        print('Schools by city:')
        for key ,value in city_name.items():
            print(f'{key}: {value}')

    elif question_no == 6:
        #QUES(6):- Search Feature base on school, city, state:-
        search_key = 'HOOVER'
        search_re = obj.search_by_value(search_key)
        for row in search_re:
            print(f"school: {row['school']} state:- {row['state']} city:- {row['city']}")


