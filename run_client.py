import pandas as pd
import json
import requests
import traceback
import warnings

warnings.simplefilter("ignore")


def get_prediction(obj: pd.DataFrame):
    try:
        resp = requests.post(url='http://localhost:5000/predict', json=json.dumps(obj))
        return resp
    except:
        return str(traceback.format_exc())


if __name__ == '__main__':
    df = pd.read_csv("X_test.csv")
    for i in range(df.shape[0]-1)[:10]:
        obj_ = df[i:i+1]
        obj = {}
        for column in df.columns:
            obj[column] = list(obj_[column])
        print('\n', obj)
        resp = get_prediction(obj=obj)
        try:
            result = json.loads(resp.text)
            print(result, resp.text)
        except:
            pass
