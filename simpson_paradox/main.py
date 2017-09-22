from __future__ import division
import pandas as pd


def department_analysis(df, gender, dept):
    pop = df.groupby(["Gender", "Dept"]).get_group((gender, dept))['Freq'].sum()
    admitted_pop = (
        df.groupby(["Gender", "Dept", "Admit"])
        .get_group((gender, dept, 'Admitted'))['Freq'].sum()
    )
    return (gender, admitted_pop / pop)

def global_population_analysis(df, gender):
    population = df.groupby("Gender").get_group(gender)['Freq'].sum()
    admitted_pop = (
        df.groupby(["Gender", "Admit"])
        .get_group((gender, 'Admitted'))['Freq'].sum()
    )
    return admitted_pop / population


def main():
    with open("./Berkeley.csv", "r") as csvfile:
        # FYI df is dataframe
        df = pd.read_csv(csvfile, header=0)
        print df

        # dept_a_df = df[df['Dept'].isin(departments)]
        # print dept_a_df
        # departments_df = [df[df['Dept'] == x] for x in departments]

        # df_group = df.groupby(["Gender"])

        # print global_population_analysis(df, "Male")
        # print global_population_analysis(df, "Female")
        #
        # departments = ['A', 'B', 'C', 'D', 'E', 'F']
        # male_department_results = [department_analysis(df, 'Male', x) for x in departments]
        # female_department_results = [department_analysis(df, 'Female', x) for x in departments]
        # print male_department_results
        # print female_department_results


        print "\n"
        print df[df['Gender'] == 'Female'][df.Admit == "Admitted"]["Freq"].sum()

        getFemales = [df['Gender'] == 'Female']
        getAdmitted = [df.Admit == "Admitted"]
        print df.loc([getFemales, getAdmitted, "Freq"])
        print df[df['Gender'] == 'Female']


main()
