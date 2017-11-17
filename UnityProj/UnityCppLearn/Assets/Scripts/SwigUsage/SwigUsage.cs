using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class SwigUsage : MonoBehaviour {

    [SerializeField]
    private Text countNumberText;

    private int number;

    void Awake()
    {
        countNumberText = GetComponent<Text>();
        TestVector();
        TestPointer();
        TestInt();
    }

    void Update()
    {
        TestSwig swig = new TestSwig();
        FooObject obj = new FooObject();
        obj.a = 1;
        //测试普通对象使用
        int i = swig.UseFool(obj);
        number = TestSwig.Add(number, i);
        countNumberText.text = number.ToString();
    }

    private void TestVector()
    {
        //申请新的Vector
        BoolVector boolVector = new BoolVector(new List<bool>()
        {
            true,
            false
        });

        //测试Vector
        for (int i = 0; i < boolVector.Count; i++)
        {
            Debug.Log(boolVector[i]);
        }
    }

    private void TestPointer()
    {
        //申请新的指针
        BoolPointer boolPointer = new BoolPointer();
        boolPointer.assign(true);
        //测试指针使用
        Debug.Log(boolPointer.value());
    }

    private void TestInt()
    {
        int length = 5;
        IntArray intArray = new IntArray(length);
        for (int i = 0; i < length; i++)
        {
            intArray.setitem(i, i * i);
        }
        for (int i = 0; i < length; i++)
        {
            Debug.Log(intArray.getitem(i).ToString());
        }
    }
}
