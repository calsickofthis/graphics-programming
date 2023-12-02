using System.Collections;
using System.Collections.Generic;
using UnityEngine;

// input namespace
using UnityEngine.InputSystem;


public class PlayerController : MonoBehaviour
{

    private Rigidbody rb;
    private float movementX;
    private float movementY;

    void Start()
    {
	rb = GetComponent<Rigidbody>();
    }

    void OnMove(InputValue movementValue)
    {
    	Vector2 movementVector = movementValue.Get<Vector2>();

	movementX = movementVector.x;
	movementY = movementVector.y;
		
    }

    void FixedUpdate()
    {
	Vector3 movement = new Vector3(movementX, 0.0f, movementY);
	
 	rb.AddForce(movement);

        //Load a scene by the name "SceneName" if you press the W key.
        if(Input.GetKeyDown(KeyCode.C)){
            Application.LoadLevel("Load Page");
        }
    }
}