using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class HelloSwig : MonoBehaviour
{
    [SerializeField]
    private Text countNumberText;

    private int number;

    void Awake()
    {
        countNumberText = GetComponent<Text>();
    }

    void Update()
    {
        number = TestSwig.Add(number, 1);
        countNumberText.text = number.ToString();
    }
}
