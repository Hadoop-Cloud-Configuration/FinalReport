package main
import(
	"fmt"
	"os"
	"runtime"
)
func ColorPrint(str string,color string){
	if runtime.GOOS=="windows"{
		fmt.Println(str)
		return
	}
	if color=="red"{
		fmt.Println("\x1b[31;1m"+str+"\x1b[0m")
	}else if color=="green"{
		fmt.Println("\x1b[32;1m"+str+"\x1b[0m")
	}else if color=="blue"{
		fmt.Println("\x1b[34;1m"+str+"\x1b[0m")
	} else{
		fmt.Println("\x1b[30;1m"+str+"\x1b[0m")
	}
}

func Check(e error) {//check all err
    if e != nil {
        panic(e)
		os.Exit(1)
    }
}
func CheckOk(ok bool){// check type assertion result
	if ok==false {
		panic("Change Type Error!")
		os.Exit(1)
	}
}

func GetHome() string{//get home directory
	if runtime.GOOS == "windows" {
			home := os.Getenv("HOMEDRIVE") + os.Getenv("HOMEPATH")
			if home == "" {
				home = os.Getenv("USERPROFILE")
			}
			return home
		}

		return os.Getenv("HOME")
}
