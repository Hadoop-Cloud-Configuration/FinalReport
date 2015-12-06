package main
import(
	"log"
    "fmt"
    "github.com/aws/aws-sdk-go/aws"
    "github.com/aws/aws-sdk-go/service/ec2"
)

func describe(Inputregion string){

	svc := ec2.New(&aws.Config{Region: aws.String(Inputregion)})

    // Call the DescribeInstances Operation
    resp, err := svc.DescribeInstances(nil)
    if err != nil {
        panic(err)
    }

    // resp has all of the response data, pull out instance IDs:
    fmt.Println("> Number of reservation sets: ", len(resp.Reservations))
    for idx, res := range resp.Reservations {
        fmt.Println("  > Number of instances: ", len(res.Instances))
        for _, inst := range resp.Reservations[idx].Instances {
            fmt.Println("    - Instance ID: ", *inst.InstanceId)
        }
    }

}

func createAWSInstance(region string, ImageId string, InstanceType string, keyName string) (interface{}){

	svc := ec2.New(&aws.Config{Region: aws.String(region)})

	params := &ec2.RunInstancesInput{
    	ImageId:      aws.String(ImageId),
    	InstanceType: aws.String(InstanceType),
    	MinCount:     aws.Int64(1),
    	MaxCount:     aws.Int64(1),
	KeyName:      aws.String(keyName),
	}

	runResult, err := svc.RunInstances(params)
	if err != nil {
    		log.Println("Could not create instance", err)
    		return err
	}

	fmt.Println(runResult)
	return runResult
}

func stopAWSInstance(Inputregion string,InstanceId string){

	svc := ec2.New(&aws.Config{Region: aws.String(Inputregion)})
	params := &ec2.StopInstancesInput{
		InstanceIds: []*string{ // Required
			aws.String(InstanceId), // Required
			// More values...
		},
		DryRun: aws.Bool(false),
		Force:  aws.Bool(true),

	}
	resp, err := svc.StopInstances(params)

	if err != nil {
	// Print the error, cast err to awserr.Error to get the Code and
	// Message from an error.
		fmt.Println(err.Error())
		return
	}

	// Pretty-print the response data.
	fmt.Println(resp)
}

