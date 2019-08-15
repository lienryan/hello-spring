package org.launchcode.hellospring.controllers;


import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.HttpServletRequest;

@Controller

public class HelloController {
    @RequestMapping(value = "")
    @ResponseBody
    public String index(HttpServletRequest request){

        String name = request.getParameter("name");

        if (name ==null) {
            name = "World";
        }
        return "Hello " +name;
    }


    //@RequestMapping(value = "hello", method= RequestMethod.GET)
    //@ResponseBody


    @RequestMapping(value = "hello/{name}")
    @ResponseBody
    public String helloUrlSegment(@PathVariable String name) {
        return "hello "+ name;

    }

    @RequestMapping(value = "hello", method= RequestMethod.POST)
    @ResponseBody
    public String helloPost(HttpServletRequest request) {
        String name = request.getParameter("name");
        return "Hello "+ name;

    }

    @RequestMapping(value="goodbye")
    public String goodbye(){
        return "redirect:/";
    }
}
