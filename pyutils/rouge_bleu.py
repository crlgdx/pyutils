from collections import Counter
from .rouge_bleu_metric.bleu import Bleu
from .rouge_bleu_metric.rouge import Rouge


class RougeL(object):
    def __init__(self, gamma=1.2):
        self.gamma = gamma  # gamma 为常量
        self.inst_scores = []
        self.r_scores = []
        self.p_scores = []

    def _lcs(self, x, y):
        """
        Computes the length of the longest common subsequence (lcs) between two
        strings. The implementation below uses a DP programming algorithm and runs
        in O(nm) time where n = len(x) and m = len(y).
        Source: http://www.algorithmist.com/index.php/Longest_Common_Subsequence
        Args:
          x: collection of words
          y: collection of words
        Returns:
          Table of dictionary of coord and len lcs
        """
        n, m = len(x), len(y)
        table = dict()
        for i in range(n + 1):
            for j in range(m + 1):
                if i == 0 or j == 0:
                    table[i, j] = 0
                elif x[i - 1] == y[j - 1]:
                    table[i, j] = table[i - 1, j - 1] + 1
                else:
                    table[i, j] = max(table[i - 1, j], table[i, j - 1])

        return table

    def lcs(self, x, y):
        """
        Returns the length of the Longest Common Subsequence between sequences x
        and y.
        Source: http://www.algorithmist.com/index.php/Longest_Common_Subsequence
        Args:
          x: sequence of words
          y: sequence of words
        Returns
          integer: Length of LCS between x and y
        """
        table = self._lcs(x, y)
        n, m = len(x), len(y)
        return table[n, m]

    def get_rougl_score(self, cand: str, ref: str):
        """
        输入单条的预测与候选答案，返回rougl得分
        :param cand:
        :param ref:
        :return:
        """
        basic_lcs = self.lcs(cand, ref)
        p_denom = len(cand)
        r_denom = len(ref)
        prec = basic_lcs / p_denom if p_denom > 0. else 0.
        rec = basic_lcs / r_denom if r_denom > 0. else 0.
        if prec != 0 and rec != 0:
            score = ((1 + self.gamma ** 2) * prec * rec) / \
                    float(rec + self.gamma ** 2 * prec)
        else:
            score = 0
        return score

    def add_inst(self, cand: str, ref: str):
        """根据参考答案分析出预测答案的分数

        Arguments:
            cand {str} -- 预测答案
            ref {str} -- 参考答案
        """

        basic_lcs = self.lcs(cand, ref)
        p_denom = len(cand)
        r_denom = len(ref)
        prec = basic_lcs / p_denom if p_denom > 0. else 0.
        rec = basic_lcs / r_denom if r_denom > 0. else 0.
        if prec != 0 and rec != 0:
            score = ((1 + self.gamma ** 2) * prec * rec) / \
                    float(rec + self.gamma ** 2 * prec)
        else:
            score = 0
        self.inst_scores.append(score)
        self.r_scores.append(rec)
        self.p_scores.append(prec)

    def get_score(self) -> float:
        """计算cand预测数据的RougeL分数

        Returns:
            float -- RougeL分数
        """
        return 1. * sum(self.inst_scores) / len(self.inst_scores)


def compute_bleu_rouge(pred_dict, ref_dict, bleu_order=4):
    """
    Compute bleu and rouge scores.
    """
    assert set(pred_dict.keys()) == set(ref_dict.keys()), \
            "missing keys: {}".format(set(ref_dict.keys()) - set(pred_dict.keys()))
    scores = {}
    bleu_scores, _ = Bleu(bleu_order).compute_score(ref_dict, pred_dict)
    for i, bleu_score in enumerate(bleu_scores):
        scores['Bleu-%d' % (i + 1)] = bleu_score
    rouge_score, _ = Rouge().compute_score(ref_dict, pred_dict)
    scores['Rouge-L'] = rouge_score
    return scores
