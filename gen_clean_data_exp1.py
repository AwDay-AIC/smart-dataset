import pandas as pd

FEATURE_COLUMNS = ['job_title', 'career_level', 'education_level', 'employment_type', 'job_benefits', 'job_description']

def _extract_feature(row):
    ret = ''
    for feature_column in FEATURE_COLUMNS:
        ret += str(row[feature_column]) + ' '

    return ret

df = pd.read_csv('raw/Jog_Description_and_Salary_in_Indonesia/test.csv', sep='|')

extracted = df[:10].apply(_extract_feature, axis=1)

output = []
for data in extracted:
    print(data)
    y = input('>> ')
    output.append({'x': data, 'y': y})

df_output = pd.DataFrame(output)
df_output.to_csv('clean/Jog_Description_and_Salary_in_Indonesia-10.csv', index=False)
