Action()
{

    /*
    web_reg_save_param("error", "LB=", "RB=", "Search=Body", LAST);
    web_custom_request(
        "lsm report", //request name
        "Method=POST",//request method
        "URL=http://10.5.0.57:9520/distribute/peers/00010026677EDF419E78CEB4C4285D17", //url
        "RecContentType=application/json", //Accept for header
        "EncType=application/json", //Content-Type for header
        "Mode=HTML",
        "Body={\"lsmSize\":7314,\"universe\":false,\"files\":[{\"file_id\":\"99BE92DB4AC56354E9D68170ED679601\",\"ppc\":12,\"sliceMap\":\"0000000000000000\"}]}",
        "LAST"
    );
    lr_output_message(lr_eval_string("{error}"));
    */

    //generate rand number,  10% request send i<n, 90% request send i=n
	// please see performance test design specification
	
	

	int rNum = 0;
	int i = 1;
	int n = 200;    // need to be updated
	char *url;
	int HttpRetCode;
    srand(time(NULL));
    rNum = rand()%10;

	lr_start_transaction("live-tag");

	if (rNum == 1) {
		i = 1;
		//url = "URL=http://live-tag.cloutropy.com/live/files/5EFAABCE8378FD2CB9961282223082B6/segments?seq=1";
		url = "URL=http://live-tag1.cloutropy.com:9662/live/files/EAC68EDF2D7629F1A092535ECA530D74/segments?seq=1";
        lr_think_time(1.5);
	} else {
		i = n;
		//url = "URL=http://live-tag.cloutropy.com/live/files/5EFAABCE8378FD2CB9961282223082B6/segments?seq=2000000";
		url = "URL=http://live-tag1.cloutropy.com:9662/live/files/EAC68EDF2D7629F1A092535ECA530D74/segments?seq=2000000";
	}
	//lr_output_message(url);

	web_reg_save_param("error", "LB=", "RB=", "Search=Body", LAST);
	/* web_custom_request(
        "Live-tag get m3u8 segment", //request name
        "Method=GET",//request method
         url, //url
        "RecContentType=application/json", //Accept for header
        "LAST"
    ); */
	

    web_url("live-tag",url, LAST);

	HttpRetCode = web_get_int_property(HTTP_INFO_RETURN_CODE);
	if (HttpRetCode == 200) {	

		//lr_log_message("Status code is: %d", HttpRetCode);
	   lr_end_transaction("live-tag", LR_PASS);
	}
    else {	
       lr_error_message("Status code is: %d", HttpRetCode);
	   lr_end_transaction("live-tag", LR_FAIL);
	}


	
	//lr_output_message(lr_eval_string("{error}"));
	
	//lr_end_transaction("live-tag", LR_AUTO);

	return 0;
}

