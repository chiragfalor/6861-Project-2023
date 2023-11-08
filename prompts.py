from itertools import product
import json
import pandas as pd
import pdb
import re
import csv

def getMaleNames():
    # maleNames taken from https://www2.census.gov/topics/genealogy/1990surnames/dist.male.first
    # 1219 entries... do you really need that many?!?
    maleNames = ['James', 'John', 'Robert', 'Michael', 'William', 'David', 'Richard', 'Charles', 'Joseph', 'Thomas', 'Christopher', 'Daniel', 'Paul', 'Mark', 'Donald', 'George', 'Kenneth', 'Steven', 'Edward', 'Brian', 'Ronald', 'Anthony', 'Kevin', 'Jason', 'Matthew', 'Gary', 'Timothy', 'Jose', 'Larry', 'Jeffrey', 'Frank', 'Scott', 'Eric', 'Stephen', 'Andrew', 'Raymond', 'Gregory', 'Joshua', 'Jerry', 'Dennis', 'Walter', 'Patrick', 'Peter', 'Harold', 'Douglas', 'Henry', 'Carl', 'Arthur', 'Ryan', 'Roger', 'Joe', 'Juan', 'Jack', 'Albert', 'Jonathan', 'Justin', 'Terry', 'Gerald', 'Keith', 'Samuel', 'Willie', 'Ralph', 'Lawrence', 'Nicholas', 'Roy', 'Benjamin', 'Bruce', 'Brandon', 'Adam', 'Harry', 'Fred', 'Wayne', 'Billy', 'Steve', 'Louis', 'Jeremy', 'Aaron', 'Randy', 'Howard', 'Eugene', 'Carlos', 'Russell', 'Bobby', 'Victor', 'Martin', 'Ernest', 'Phillip', 'Todd', 'Jesse', 'Craig', 'Alan', 'Shawn', 'Clarence', 'Sean', 'Philip', 'Chris', 'Johnny', 'Earl', 'Jimmy', 'Antonio', 'Danny', 'Bryan', 'Tony', 'Luis', 'Mike', 'Stanley', 'Leonard', 'Nathan', 'Dale', 'Manuel', 'Rodney', 'Curtis', 'Norman', 'Allen', 'Marvin', 'Vincent', 'Glenn', 'Jeffery', 'Travis', 'Jeff', 'Chad', 'Jacob', 'Lee', 'Melvin', 'Alfred', 'Kyle', 'Francis', 'Bradley', 'Jesus', 'Herbert', 'Frederick', 'Ray', 'Joel', 'Edwin', 'Don', 'Eddie', 'Ricky', 'Troy', 'Randall', 'Barry', 'Alexander', 'Bernard', 'Mario', 'Leroy', 'Francisco', 'Marcus', 'Micheal', 'Theodore', 'Clifford', 'Miguel', 'Oscar', 'Jay', 'Jim', 'Tom', 'Calvin', 'Alex', 'Jon', 'Ronnie', 'Bill', 'Lloyd', 'Tommy', 'Leon', 'Derek', 'Warren', 'Darrell', 'Jerome', 'Floyd', 'Leo', 'Alvin', 'Tim', 'Wesley', 'Gordon', 'Dean', 'Greg', 'Jorge', 'Dustin', 'Pedro', 'Derrick', 'Dan', 'Lewis', 'Zachary', 'Corey', 'Herman', 'Maurice', 'Vernon', 'Roberto', 'Clyde', 'Glen', 'Hector', 'Shane', 'Ricardo', 'Sam', 'Rick', 'Lester', 'Brent', 'Ramon', 'Charlie', 'Tyler', 'Gilbert', 'Gene', 'Marc', 'Reginald', 'Ruben', 'Brett', 'Angel', 'Nathaniel', 'Rafael', 'Leslie', 'Edgar', 'Milton', 'Raul', 'Ben', 'Chester', 'Cecil', 'Duane', 'Franklin', 'Andre', 'Elmer', 'Brad', 'Gabriel', 'Ron', 'Mitchell', 'Roland', 'Arnold', 'Harvey', 'Jared', 'Adrian', 'Karl', 'Cory', 'Claude', 'Erik', 'Darryl', 'Jamie', 'Neil', 'Jessie', 'Christian', 'Javier', 'Fernando', 'Clinton', 'Ted', 'Mathew', 'Tyrone', 'Darren', 'Lonnie', 'Lance', 'Cody', 'Julio', 'Kelly', 'Kurt', 'Allan', 'Nelson', 'Guy', 'Clayton', 'Hugh', 'Max', 'Dwayne', 'Dwight', 'Armando', 'Felix', 'Jimmie', 'Everett', 'Jordan', 'Ian', 'Wallace', 'Ken', 'Bob', 'Jaime', 'Casey', 'Alfredo', 'Alberto', 'Dave', 'Ivan', 'Johnnie', 'Sidney', 'Byron', 'Julian', 'Isaac', 'Morris', 'Clifton', 'Willard', 'Daryl', 'Ross', 'Virgil', 'Andy', 'Marshall', 'Salvador', 'Perry', 'Kirk', 'Sergio', 'Marion', 'Tracy', 'Seth', 'Kent', 'Terrance', 'Rene', 'Eduardo', 'Terrence', 'Enrique', 'Freddie', 'Wade', 'Austin', 'Stuart', 'Fredrick', 'Arturo', 'Alejandro', 'Jackie', 'Joey', 'Nick', 'Luther', 'Wendell', 'Jeremiah', 'Evan', 'Julius', 'Dana', 'Donnie', 'Otis', 'Shannon', 'Trevor', 'Oliver', 'Luke', 'Homer', 'Gerard', 'Doug', 'Kenny', 'Hubert', 'Angelo', 'Shaun', 'Lyle', 'Matt', 'Lynn', 'Alfonso', 'Orlando', 'Rex', 'Carlton', 'Ernesto', 'Cameron', 'Neal', 'Pablo', 'Lorenzo', 'Omar', 'Wilbur', 'Blake', 'Grant', 'Horace', 'Roderick', 'Kerry', 'Abraham', 'Willis', 'Rickey', 'Jean', 'Ira', 'Andres', 'Cesar', 'Johnathan', 'Malcolm', 'Rudolph', 'Damon', 'Kelvin', 'Rudy', 'Preston', 'Alton', 'Archie', 'Marco', 'Wm', 'Pete', 'Randolph', 'Garry', 'Geoffrey', 'Jonathan', 'Felipe', 'Bennie', 'Gerardo', 'Ed', 'Dominic', 'Robin', 'Loren', 'Delbert', 'Colin', 'Guillermo', 'Earnest', 'Lucas', 'Benny', 'Noel', 'Spencer', 'Rodolfo', 'Myron', 'Edmund', 'Garrett', 'Salvatore', 'Cedric', 'Lowell', 'Gregg', 'Sherman', 'Wilson', 'Devin', 'Sylvester', 'Kim', 'Roosevelt', 'Israel', 'Jermaine', 'Forrest', 'Wilbert', 'Leland', 'Simon', 'Guadalupe', 'Clark', 'Irving', 'Carroll', 'Bryant', 'Owen', 'Rufus', 'Woodrow', 'Sammy', 'Kristopher', 'Mack', 'Levi', 'Marcos', 'Gustavo', 'Jake', 'Lionel', 'Marty', 'Taylor', 'Ellis', 'Dallas', 'Gilberto', 'Clint', 'Nicolas', 'Laurence', 'Ismael', 'Orville', 'Drew', 'Jody', 'Ervin', 'Dewey', 'Al', 'Wilfred', 'Josh', 'Hugo', 'Ignacio', 'Caleb', 'Tomas', 'Sheldon', 'Erick', 'Frankie', 'Stewart', 'Doyle', 'Darrel', 'Rogelio', 'Terence', 'Santiago', 'Alonzo', 'Elias', 'Bert', 'Elbert', 'Ramiro', 'Conrad', 'Pat', 'Noah', 'Grady', 'Phil', 'Cornelius', 'Lamar', 'Rolando', 'Clay', 'Percy', 'Dexter', 'Bradford', 'Merle', 'Darin', 'Amos', 'Terrell', 'Moses', 'Irvin', 'Saul', 'Roman', 'Darnell', 'Randal', 'Tommie', 'Timmy', 'Darrin', 'Winston', 'Brendan', 'Toby', 'Van', 'Abel', 'Dominick', 'Boyd', 'Courtney', 'Jan', 'Emilio', 'Elijah', 'Cary', 'Domingo', 'Santos', 'Aubrey', 'Emmett', 'Marlon', 'Emanuel', 'Jerald', 'Edmond', 'Emil', 'Dewayne', 'Will', 'Otto', 'Teddy', 'Reynaldo', 'Bret', 'Morgan', 'Jess', 'Trent', 'Humberto', 'Emmanuel', 'Stephan', 'Louie', 'Vicente', 'Lamont', 'Stacy', 'Garland', 'Miles', 'Micah', 'Efrain', 'Billie', 'Logan', 'Heath', 'Rodger', 'Harley', 'Demetrius', 'Ethan', 'Eldon', 'Rocky', 'Pierre', 'Junior', 'Freddy', 'Eli', 'Bryce', 'Antoine', 'Robbie', 'Kendall', 'Royce', 'Sterling', 'Mickey', 'Chase', 'Grover', 'Elton', 'Cleveland', 'Dylan', 'Chuck', 'Damian', 'Reuben', 'Stan', 'August', 'Leonardo', 'Jasper', 'Russel', 'Erwin', 'Benito', 'Hans', 'Monte', 'Blaine', 'Ernie', 'Curt', 'Quentin', 'Agustin', 'Murray', 'Jamal', 'Devon', 'Adolfo', 'Harrison', 'Tyson', 'Burton', 'Brady', 'Elliott', 'Wilfredo', 'Bart', 'Jarrod', 'Vance', 'Denis', 'Damien', 'Joaquin', 'Harlan', 'Desmond', 'Elliot', 'Darwin', 'Ashley', 'Gregorio', 'Buddy', 'Xavier', 'Kermit', 'Roscoe', 'Esteban', 'Anton', 'Solomon', 'Scotty', 'Norbert', 'Elvin', 'Williams', 'Nolan', 'Carey', 'Rod', 'Quinton', 'Hal', 'Brain', 'Rob', 'Elwood', 'Kendrick', 'Darius', 'Moises', 'Son', 'Marlin', 'Fidel', 'Thaddeus', 'Cliff', 'Marcel', 'Ali', 'Jackson', 'Raphael', 'Bryon', 'Armand', 'Alvaro', 'Jeffry', 'Dane', 'Joesph', 'Thurman', 'Ned', 'Sammie', 'Rusty', 'Michel', 'Monty', 'Rory', 'Fabian', 'Reggie', 'Mason', 'Graham', 'Kris', 'Isaiah', 'Vaughn', 'Gus', 'Avery', 'Loyd', 'Diego', 'Alexis', 'Adolph', 'Norris', 'Millard', 'Rocco', 'Gonzalo', 'Derick', 'Rodrigo', 'Gerry', 'Stacey', 'Carmen', 'Wiley', 'Rigoberto', 'Alphonso', 'Ty', 'Shelby', 'Rickie', 'Noe', 'Vern', 'Bobbie', 'Reed', 'Jefferson', 'Elvis', 'Bernardo', 'Mauricio', 'Hiram', 'Donovan', 'Basil', 'Riley', 'Ollie', 'Nickolas', 'Maynard', 'Scot', 'Vince', 'Quincy', 'Eddy', 'Sebastian', 'Federico', 'Ulysses', 'Heriberto', 'Donnell', 'Cole', 'Denny', 'Davis', 'Gavin', 'Emery', 'Ward', 'Romeo', 'Jayson', 'Dion', 'Dante', 'Clement', 'Coy', 'Odell', 'Maxwell', 'Jarvis', 'Bruno', 'Issac', 'Mary', 'Dudley', 'Brock', 'Sanford', 'Colby', 'Carmelo', 'Barney', 'Nestor', 'Hollis', 'Stefan', 'Donny', 'Art', 'Linwood', 'Beau', 'Weldon', 'Galen', 'Isidro', 'Truman', 'Delmar', 'Johnathon', 'Silas', 'Frederic', 'Dick', 'Kirby', 'Irwin', 'Cruz', 'Merlin', 'Merrill', 'Charley', 'Marcelino', 'Lane', 'Harris', 'Cleo', 'Carlo', 'Trenton', 'Kurtis', 'Hunter', 'Aurelio', 'Winfred', 'Vito', 'Collin', 'Denver', 'Carter', 'Leonel', 'Emory', 'Pasquale', 'Mohammad', 'Mariano', 'Danial', 'Blair', 'Landon', 'Dirk', 'Branden', 'Adan', 'Numbers', 'Clair', 'Buford', 'German', 'Bernie', 'Wilmer', 'Joan', 'Emerson', 'Zachery', 'Fletcher', 'Jacques', 'Errol', 'Dalton', 'Monroe', 'Josue', 'Dominique', 'Edwardo', 'Booker', 'Wilford', 'Sonny', 'Shelton', 'Carson', 'Theron', 'Raymundo', 'Daren', 'Tristan', 'Houston', 'Robby', 'Lincoln', 'Jame', 'Genaro', 'Gale', 'Bennett', 'Octavio', 'Cornell', 'Laverne', 'Hung', 'Arron', 'Antony', 'Herschel', 'Alva', 'Giovanni', 'Garth', 'Cyrus', 'Cyril', 'Ronny', 'Stevie', 'Lon', 'Freeman', 'Erin', 'Duncan', 'Kennith', 'Carmine', 'Augustine', 'Young', 'Erich', 'Chadwick', 'Wilburn', 'Russ', 'Reid', 'Myles', 'Anderson', 'Morton', 'Jonas', 'Forest', 'Mitchel', 'Mervin', 'Zane', 'Rich', 'Jamel', 'Lazaro', 'Alphonse', 'Randell', 'Major', 'Johnie', 'Jarrett', 'Brooks', 'Ariel', 'Abdul', 'Dusty', 'Luciano', 'Lindsey', 'Tracey', 'Seymour', 'Scottie', 'Eugenio', 'Mohammed', 'Sandy', 'Valentin', 'Chance', 'Arnulfo', 'Lucien', 'Ferdinand', 'Thad', 'Ezra', 'Sydney', 'Aldo', 'Rubin', 'Royal', 'Mitch', 'Earle', 'Abe', 'Wyatt', 'Marquis', 'Lanny', 'Kareem', 'Jamar', 'Boris', 'Isiah', 'Emile', 'Elmo', 'Aron', 'Leopoldo', 'Everette', 'Josef', 'Gail', 'Eloy', 'Dorian', 'Rodrick', 'Reinaldo', 'Lucio', 'Jerrod', 'Weston', 'Hershel', 'Barton', 'Parker', 'Lemuel', 'Lavern', 'Burt', 'Jules', 'Gil', 'Eliseo', 'Ahmad', 'Nigel', 'Efren', 'Antwan', 'Alden', 'Margarito', 'Coleman', 'Refugio', 'Dino', 'Osvaldo', 'Les', 'Deandre', 'Normand', 'Kieth', 'Ivory', 'Andrea', 'Trey', 'Norberto', 'Napoleon', 'Jerold', 'Fritz', 'Rosendo', 'Milford', 'Sang', 'Deon', 'Christoper', 'Alfonzo', 'Lyman', 'Josiah', 'Brant', 'Wilton', 'Rico', 'Jamaal', 'Dewitt', 'Carol', 'Brenton', 'Yong', 'Olin', 'Foster', 'Faustino', 'Claudio', 'Judson', 'Gino', 'Edgardo', 'Berry', 'Alec', 'Tanner', 'Jarred', 'Donn', 'Trinidad', 'Tad', 'Shirley', 'Prince', 'Porfirio', 'Odis', 'Maria', 'Lenard', 'Chauncey', 'Chang', 'Tod', 'Mel', 'Marcelo', 'Kory', 'Augustus', 'Keven', 'Hilario', 'Bud', 'Sal', 'Rosario', 'Orval', 'Mauro', 'Dannie', 'Zachariah', 'Olen', 'Anibal', 'Milo', 'Jed', 'Frances', 'Thanh', 'Dillon', 'Amado', 'Newton', 'Connie', 'Lenny', 'Tory', 'Richie', 'Lupe', 'Horacio', 'Brice', 'Mohamed', 'Delmer', 'Dario', 'Reyes', 'Dee', 'Mac', 'Jonah', 'Jerrold', 'Robt', 'Hank', 'Sung', 'Rupert', 'Rolland', 'Kenton', 'Damion', 'Chi', 'Antone', 'Waldo', 'Fredric', 'Bradly', 'Quinn', 'Kip', 'Burl', 'Walker', 'Tyree', 'Jefferey', 'Ahmed', 'Willy', 'Stanford', 'Oren', 'Noble', 'Moshe', 'Mikel', 'Enoch', 'Brendon', 'Quintin', 'Jamison', 'Florencio', 'Darrick', 'Tobias', 'Minh', 'Hassan', 'Giuseppe', 'Demarcus', 'Cletus', 'Tyrell', 'Lyndon', 'Keenan', 'Werner', 'Theo', 'Geraldo', 'Lou', 'Columbus', 'Chet', 'Bertram', 'Markus', 'Huey', 'Hilton', 'Dwain', 'Donte', 'Tyron', 'Omer', 'Isaias', 'Hipolito', 'Fermin', 'Chung', 'Adalberto', 'Valentine', 'Jamey', 'Bo', 'Barrett', 'Whitney', 'Teodoro', 'Mckinley', 'Maximo', 'Garfield', 'Sol', 'Raleigh', 'Lawerence', 'Abram', 'Rashad', 'King', 'Emmitt', 'Daron', 'Chong', 'Samual', 'Paris', 'Otha', 'Miquel', 'Lacy', 'Eusebio', 'Dong', 'Domenic', 'Darron', 'Buster', 'Antonia', 'Wilber', 'Renato', 'Jc', 'Hoyt', 'Haywood', 'Ezekiel', 'Chas', 'Florentino', 'Elroy', 'Clemente', 'Arden', 'Neville', 'Kelley', 'Edison', 'Deshawn', 'Carrol', 'Shayne', 'Nathanial', 'Jordon', 'Danilo', 'Claud', 'Val', 'Sherwood', 'Raymon', 'Rayford', 'Cristobal', 'Ambrose', 'Titus', 'Hyman', 'Felton', 'Ezequiel', 'Erasmo', 'Stanton', 'Lonny', 'Len', 'Ike', 'Milan', 'Lino', 'Jarod', 'Herb', 'Andreas', 'Walton', 'Rhett', 'Palmer', 'Jude', 'Douglass', 'Cordell', 'Oswaldo', 'Ellsworth', 'Virgilio', 'Toney', 'Nathanael', 'Del', 'Britt', 'Benedict', 'Mose', 'Hong', 'Leigh', 'Johnson', 'Isreal', 'Gayle', 'Garret', 'Fausto', 'Asa', 'Arlen', 'Zack', 'Warner', 'Modesto', 'Francesco', 'Manual', 'Jae', 'Gaylord', 'Gaston', 'Filiberto', 'Deangelo', 'Michale', 'Granville', 'Wes', 'Malik', 'Zackary', 'Tuan', 'Nicky', 'Eldridge', 'Cristopher', 'Cortez', 'Antione', 'Malcom', 'Long', 'Korey', 'Jospeh', 'Colton', 'Waylon', 'Von', 'Hosea', 'Shad', 'Santo', 'Rudolf', 'Rolf', 'Rey', 'Renaldo', 'Marcellus', 'Lucius', 'Lesley', 'Kristofer', 'Boyce', 'Benton', 'Man', 'Kasey', 'Jewell', 'Hayden', 'Harland', 'Arnoldo', 'Rueben', 'Leandro', 'Kraig', 'Jerrell', 'Jeromy', 'Hobert', 'Cedrick', 'Arlie', 'Winford', 'Wally', 'Patricia', 'Luigi', 'Keneth', 'Jacinto', 'Graig', 'Franklyn', 'Edmundo', 'Sid', 'Porter', 'Leif', 'Lauren', 'Jeramy', 'Elisha', 'Buck', 'Willian', 'Vincenzo', 'Shon', 'Michal', 'Lynwood', 'Lindsay', 'Jewel', 'Jere', 'Hai', 'Elden', 'Dorsey', 'Darell', 'Broderick', 'Alonso']

    return maleNames

def getPlayerString(team, names):
    if len(team) == 1: 
        str_team = names[(team[0]) - 1]
    elif len(team) == 2:
        str_team = "a team of " + names[(team[0]) - 1] + " and " + names[(team[1]) - 1]
    else:
        str_team = "a team of "
        i = 0
        for x in team:
            if i == (len(team) - 1):
                str_team += "and " + names[x - 1]
            else:
                str_team += names[x - 1] + ", "
            i += 1
    
    return str_team

def getGameString(games, names):
    """Returns a string. Some examples include: 
    a team of players X competed against a team of players X and the team of players X won;
    player X competed against player X and player X won.
    Varies on whether or not the players are in a team."""

    if games['winner'] == 1:
        str_game = getPlayerString(games['team1'], names)
        str_game += " won against "
        str_game += getPlayerString(games['team2'], names)
        str_game += "."
    elif games['winner'] == 2:
        str_game = getPlayerString(games['team2'], names)
        str_game += " won against "
        str_game += getPlayerString(games['team1'], names)
        str_game += "."
    else:
        print("\n\nWARNING!! THE NUMBER OF TEAMS IS GREATER THAN 2!! INVESTIGATE LINE 40\n\n")

    return str_game

def getScenarioQuestion(scen, p_names):
    if scen['questions'][0] == "strength":
        ques = "a scale from 0 (very weak) to 100 (very strong), how strong is " + p_names[(scen['subjects'][0]['player']) - 1] + "?\n"
    elif scen['questions'][0] == "effort":
        ques = "a scale from 0 (low effort) to 100 (high effort), how much effort did " + p_names[(scen['subjects'][0]['player']) - 1] + " put in for Game " + str(scen['subjects'][0]['match']) + "?\n"
    elif scen['questions'][0] == "outcome":
        ques = "a scale from 0 (definitely " + p_names[(scen['subjects'][0]['team1'][0]) - 1] + ") to 100 (definitely " + p_names[(scen['subjects'][0]['team2'][0]) - 1] + "), who would win in another match?\n"

    return ques

def trialPrompt(dict, num_trial, num_examples):
    if (num_examples == 0):
        return dict[num_trial]

    if (num_trial > 0):
        return trialPrompt(dict, num_trial - 1, num_examples - 1) + dict[num_trial]
    else:
        return trialPrompt(dict, len(dict) - 1, num_examples - 1) + dict[num_trial]

fields = ["task_id","language_full","language_phrase_1","language_phrase_2","language_phrase_3","language_phrase_4","question sentence","code_phrase_1","code_phrase_2","code_phrase_3","code_phrase_4","question code"]
rows = []

def trialDict(stim_info, exp):

    # open csv file that has the avergage human responses for each trial 
    # df_avg_responses = pd.read_csv('../../data/exp' + str(exp) + '_avg_human_respnse.csv')

    # create the trial dictionary where all the trial information will be stored in english sentences ready to be read by gpt 
    trial_dict = {}
    trial_dict_with_com = {}

    maleNames = getMaleNames()
    name_index = 0
    task_id = 0
    # iterate through the scenarios (aka trials) of the experiment
    for scenario in stim_info['scenarios']:

        # scenario = stim_info['scenarios'][6]
        # get the number of players in each scenario 
        players_list = []
        for game in scenario['games']:
            for player_num in game['team1']:
                players_list.append(player_num)
            for player_num in game['team2']:
                players_list.append(player_num)
        num_players = max(players_list)

        # create a name array with the names of the players in that scenario (remember names cannot be repeated)
        player_names = []
        for i in range(name_index, name_index + num_players):
            player_names.append(maleNames[i])

        name_index += num_players

        # pass the name array to getGameString function 

        # Evidence
        game_num = 1 
        trial_str =""
        # iterate through the games for each scenario
        row = []
        row_code = []
        for game in scenario['games']:
            # creating the full, one long language string
            trial_str = trial_str + " In Game " + str(game_num) + ", "
            trial_str = trial_str + getGameString(game, player_names)
            print(" In Game " + str(game_num) + ", "+getGameString(game, player_names)) 

            # create list of one sentences
            row.append(" In Game " + str(game_num) + ", "+getGameString(game, player_names)) 

            # creating list of conditions corresponding to each sentence
            row_code.append("condition(" +f"winner({[player_names[num-1] for num in game['team1']]},{[player_names[num-1] for num in game['team2']]},{game_num}) == {game['winner']});")
            print(row_code)
            game_num += 1
        row+=[""]*(4-len(row)) 
        row_code+=[""]*(4-len(row_code)) 
        ques_exp = "Question: On a scale from 0 (very weak) to 100 (very strong), how strong is " + player_names[(scenario['subjects'][0]['player']) - 1] + "?"

        rows.append([task_id,trial_str]+row+[ques_exp]+row_code+[f"strength({player_names[scenario['subjects'][0]['player']]})"])
        task_id+=1
        
    

def extract_question(prompt):
    start_index = prompt.find('Question:')
    end_index = prompt.find('\n', start_index)
    return prompt[start_index:end_index]

def common_words(str, ary_str):
    str_words = set(str.split())
    common = []
    for s in ary_str:
        if set(s.split()).intersection(str_words):
            common.append(s)
    result = []
    for i, s in enumerate(ary_str):
        if s in common:
            score = 100 if s == common[1] else 0
            result.append((s, score))
    return result

# CHANGE EXP: 1, 2, or 3
experiment_num = 1
num_ex = 2

# open json file where the experiment stimulus is stored
file = open(".\human_exp.json")
stimulus_info = json.load(file)
trialDict(stimulus_info, 1)
file.close() # close json file
# name of csv file  
filename = "prompt_grid.csv"

# writing to csv file  
with open(filename, 'w') as csvfile:  
    # creating a csv writer object  
    csvwriter = csv.writer(csvfile)  
        
    # writing the fields  
    csvwriter.writerow(fields)  
        
    # writing the data rows  
    csvwriter.writerows(rows) 


