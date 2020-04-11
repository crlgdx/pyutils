#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   pandas_util.py    
@Contact :   cr_lgdx@163.com
@Author  :   lduml
@Modify Time      @Version    @Desciption
------------      --------    -----------
2020/4/11 4:48 下午    1.0         None
"""
import pandas as pd


def pd2json(pd_data: pd.DataFrame, orient='records'):
    """
    pandas DataFrame对象 转json对象
    :param pd_data:
    :param orient: 输出指定的json格式 默认records
    :return:
    * orient --->  The format of the JSON string
                    输出指定的json格式
              - 'split' : dict like {'index' -> [index],
                'columns' -> [columns], 'data' -> [values]}
              - 'records' : list like
                [{column -> value}, ... , {column -> value}]
              - 'index' : dict like {index -> {column -> value}}
              - 'columns' : dict like {column -> {index -> value}}
              - 'values' : just the values array
              - 'table' : dict like {'schema': {schema}, 'data': {data}}
                describing the data, and the data component is
                like ``orient='records'``.
    """
    """
    Examples
        --------

        >>> df = pd.DataFrame([['a', 'b'], ['c', 'd']],
        ...                   index=['row 1', 'row 2'],
        ...                   columns=['col 1', 'col 2'])
        >>> df.to_json(orient='split')
        '{"columns":["col 1","col 2"],
          "index":["row 1","row 2"],
          "data":[["a","b"],["c","d"]]}'

        Encoding/decoding a Dataframe using ``'records'`` formatted JSON.
        Note that index labels are not preserved with this encoding.

        >>> df.to_json(orient='records')
        '[{"col 1":"a","col 2":"b"},{"col 1":"c","col 2":"d"}]'

        Encoding/decoding a Dataframe using ``'index'`` formatted JSON:

        >>> df.to_json(orient='index')
        '{"row 1":{"col 1":"a","col 2":"b"},"row 2":{"col 1":"c","col 2":"d"}}'

        Encoding/decoding a Dataframe using ``'columns'`` formatted JSON:

        >>> df.to_json(orient='columns')
        '{"col 1":{"row 1":"a","row 2":"c"},"col 2":{"row 1":"b","row 2":"d"}}'

        Encoding/decoding a Dataframe using ``'values'`` formatted JSON:

        >>> df.to_json(orient='values')
        '[["a","b"],["c","d"]]'

        Encoding with Table Schema

        >>> df.to_json(orient='table')
        '{"schema": {"fields": [{"name": "index", "type": "string"},
                                {"name": "col 1", "type": "string"},
                                {"name": "col 2", "type": "string"}],
                     "primaryKey": "index",
                     "pandas_version": "0.20.0"},
          "data": [{"index": "row 1", "col 1": "a", "col 2": "b"},
                   {"index": "row 2", "col 1": "c", "col 2": "d"}]}'
        """

    return pd_data.to_json(orient=orient)


def json2pd(json_data):
    """
    json或者list中存在dict 转为pandas结构
    :param json_data:
    :return:
    """
    """
    Examples
    --------
    # style1 
    >> json_data = {1:['2','2','3'],3:['4','4','3']}
    >> pd.DataFrame.from_records(json_data)
    |    |   1 |   3 |
    |---:|----:|----:|
    |  0 |   2 |   4 |
    |  1 |   2 |   4 |
    |  2 |   3 |   3 |
    ---
    # style2
    >> json_data = [{3:'5',6:'5'},{3:'5',6:'5'},{3:'5',6:'5'}]
    >> pd.DataFrame.from_records(json_data)
    |    |   3 |   6 |
    |---:|----:|----:|
    |  0 |   5 |   5 |
    |  1 |   5 |   5 |
    |  2 |   5 |   5 |
    """
    return pd.DataFrame.from_records(json_data)


def pd2markdown(pd_data: pd.DataFrame):
    """
    打印pandas对象 以文本格式输出
    :param pd_data:
    :return:
    """
    """
    Examples
    --------
    >> json_data = [{3:'5',6:'5'},{3:'5',6:'5'},{3:'5',6:'5'}]
    >> pd_data = pd.DataFrame.from_records(json_data)
    >> pd2markdown(pd_data)
    |    |   3 |   6 |
    |---:|----:|----:|
    |  0 |   5 |   5 |
    |  1 |   5 |   5 |
    |  2 |   5 |   5 |
    """
    try:
        import tabulate
    except ImportError:
        print('Error ,please install tabulate')
        print('pip install tabulate')
        pass
    print(tabulate(pd_data, tablefmt="pipe", headers="keys"))
