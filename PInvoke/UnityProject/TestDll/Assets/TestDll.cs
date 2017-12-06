using System.Collections;
using System.Collections.Generic;
using System.Runtime.InteropServices;
using UnityEngine;

public class TestDll : MonoBehaviour
{

	[DllImport("TestDll")]
	private static extern int add(int a, int b);

	private int i = 0;
	
	// Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	void Update ()
	{
		i = add(i, 1);
		Debug.Log(i.ToString());
	}
}
