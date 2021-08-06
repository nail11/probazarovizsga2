
from lxml import html

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())

url = "https://witty-hill-0acfceb03.azurestaticapps.net/mutant_teams.html"

try:
    driver.get(url)
# finding and making list of the names which identifies characters

    character_list = []
    team_groups = []
    char_element = driver.find_elements_by_tag_name("li")
    for i in range(len(char_element)):
        char_name = char_element[i].text
        character_list.append(char_name)
        teams = char_element[i].get_attribute("data-teams")
        team_groups.append(teams)


    print(team_groups)

# collecting contents of each line in HTML identified by elements of "character_list"
# the text should contain the group of teams which the name belongs to

    #root = html.parse("https://witty-hill-0acfceb03.azurestaticapps.net/mutant_teams.html").getroot()
    # ez nem működik nekem

    #for j in range(len(character_list)):
       # element = root.get_element_by_id(character_list[j])
        #text_in_html_element = element.text_content()

# next steps are
    # reading out the group of teams from each "text_in_html_element"
    # making pairs from groups and names
    # checking if clicking on different selector radio buttons, the figures, which  belong to the
    # given teams, jumps out

finally:
    driver.close()

