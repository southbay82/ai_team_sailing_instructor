import os
from dotenv import load_dotenv

load_dotenv()

from financial_analyst_crew.crew import FinancialAnalystCrew

def run():
    inputs = {
        'comapny_name' : 'Tesla',
    }
    FinancialAnalystCrew().crew().kickoff(inputs=inputs)


print ('Firing up AI Crew...')
if __name__=="__main__":
    run()

