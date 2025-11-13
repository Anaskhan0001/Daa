//SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;

contract StudentData{
    struct Student{
        string name;
        uint rollno;
    }

    Student[] public studentArr;

    function addStudent(string memory name,uint rollno) public{
        for(uint i=0;i<studentArr.length;i++){
            if(studentArr[i].rollno==rollno){
                revert("Student with roll no already exists!");
            }
        }
        studentArr.push(Student(name,rollno));
    }

    function displayAllStudents() public view returns(Student[] memory){
        return studentArr;
    }

    function getStudentByIndex(uint index) public view returns(Student memory){
        require(index<studentArr.length || index > studentArr.length,"Index out of bound");
        return studentArr[index];
    }

    function getLengthOfStudents() public view returns(uint){
        return studentArr.length;
    }


}