using UnityEngine;
public class InstantiationExample : MonoBehaviour 
{
    // Reference to the Prefab. Drag a Prefab into this field in the Inspector.
    public GameObject myPrefab;
    public Rigidbody projectile;
    public float speed = 114;

    // This script will simply instantiate the Prefab when the game starts.
    void Start()
    {
    }

    void Update()
    {
        if (Input.GetKeyDown("space")){
            // Instantiate(myPrefab, new Vector3(x,y,0), Quaternion.identity);
            Rigidbody p = Instantiate(projectile, transform.position, transform.rotation);
            // Debug.Log(transform.position);
            // Debug.Log(transform.rotation);
            p.velocity = transform.forward * 200;
       }
    }
}