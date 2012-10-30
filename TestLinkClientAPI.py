'''
Created on Sep 18, 2012

@author: bryant
'''
import xmlrpclib

class TestLinkClientAPI:
    def __init__(self, server_url, devKey):
        self.server = xmlrpclib.Server(server_url)
        self.devKey = devKey
        self.stepsList = []
        
    #
    #    BUILT-IN API CALLS
    #
    
    def checkDevKey(self):
        """checkDevKey:
        Check if developer key exists
        """
        argsAPI = {'devKey':self.devKey}
        return self.server.tl.checkDevKey(argsAPI)
    
    def about(self):
        """about:
        Give basic information about the API
        """
        return self.server.tl.about()
    
    def ping(self):
        """ping
        """
        return self.server.tl.ping()
    
    def echo(self, message):
        return self.server.tl.repeat({'str':message})
    
    def doesUserExist(self, user):
        """doesUserExist:
        Check if a user name exists
        """
        argsAPI = {'devKey':self.devKey,
                 'user':str(user)}
        return self.server.tl.doesUserExist(argsAPI)
    
    def getBuildsForTestPlan(self, testplanid):
        """getBuildsForTestPlan:
        Get a list of builds within a test plan
        """
        argsAPI = {'devKey':self.devKey,
                 'testplanid':str(testplanid)}
        return self.server.tl.getBuildsForTestPlan(argsAPI)
    
    def getFirstLevelTestSuitesForTestProject(self, testprojectid):
        """getFirstLevelTestSuitesForTestProject
        Get set of test suites AT TOP LEVEL of tree on a test project
        """
        argsAPI = {'devKey':self.devKey,
                 'testprojectid':str(testprojectid)}
        return self.server.tl.getFirstLevelTestSuitesForTestProject(argsAPI)
    
    def getFullPath(self, nodeid):
        """getFullPath:
        Get full path from the given node till the top using
        nodes_hierarchy_table
        """
        argsAPI = {'devKey':self.devKey,
                 'nodeid':str(nodeid)}
        return self.server.tl.getFullPath(argsAPI)
    
    def getLastExecutionResult(self, testplanid, testcaseid):
        """getLastExecutionResult
        Get the result of LAST EXECUTION for a particular testcase on a 
        test plan, but WITHOUT checking for a particular build
        """
        argsAPI = {'devKey':self.devKey,
                 'testplanid':str(testplanid),
                 'testcaseid':str(testcaseid)}
        return self.server.tl.getLastExecutionResult(argsAPI)
    
    def getLatestBuildForTestPlan(self, testplanid):
        """getLatestBuildForTestPlan
        Get the latest build by choosing the maximum build id for a 
        specific test plan
        """
        argsAPI = {'devKey':self.devKey,
                 'testplanid':str(testplanid)}
        return self.server.tl.getLatestBuildForTestPlan(argsAPI)
    
    def getProjects(self):
        """getProjects
        Get a list of all projects
        """
        argsAPI = {'devKey':self.devKey}
        return self.server.tl.getProjects(argsAPI)
    
    def getProjectTestPlans(self, testprojectid):
        """getProjectTestPlans:
        Get a list of test plans of a specific project
        """
        argsAPI = {'devKey':self.devKey,
                 'testprojectid':str(testprojectid)}
        return self.server.tl.getProjectTestPlans(argsAPI)
    
    def getTestCase(self, testcaseid):
        """getTestCase
        Get test case specification using external or internal id
        """
        argsAPI = {'devKey':self.devKey,
                 'testcaseid':str(testcaseid)}
        return self.server.tl.getTestCase(argsAPI)
    
    def getTestCaseAttachments(self, testcaseid):
        """getTestCaseaAttachments
        Get attachments of a specified test case
        """
        argsAPI = {'devKey':self.devKey,
                 'testcaseid':str(testcaseid)}
        return self.server.tl.getTestCaseAttachments(argsAPI)
    
    def getTestCaseCustomFieldDesignValue(self, testcaseexternalid, version,
                                          testprojectid, customfieldname, details):
        """getTestCaseCustomFieldDesignValue
        Get values of a custom field with scope='design' for a given test case
        """
        argsAPI = {'devKey':self.devKey,
                 'testcaseexternalid':str(testcaseexternalid),
                 'version':str(version),
                 'testprojectid':str(testprojectid),
                 'customfieldname':str(customfieldname),
                 'details':str(details)}
        return self.server.tl.getTestCaseCustomFieldDesignValue(argsAPI)
    
    def getTestCaseIDByName(self, testcasename):
        """getTestCaseIDByName
        Find a test case by its name
        """
        argsAPI = {'devKey':self.devKey,
                 'testcasename':str(testcasename)}
        return self.server.tl.getTestCaseIDByName(argsAPI)
    
    def getTestCasesForTestPlan(self, *args):
        """getTestCasesForTestPlan:
        List test cases linked to a test plan
            Mandatory parameters: testplanid
            Optional parameters: testcaseid, buildid, keywordid, keywords,
            executed, assignedto, executestatus, executiontype, getstepinfo
        """
        testplanid = args[0]
        argsAPI = {'devKey':self.devKey,
                 'testplanid':str(testplanid)}
        if len(args) > 1:
            params = args[1:]
            for param in params:
                paramlist = param.split("=")
                argsAPI[paramlist[0]] = paramlist[1]
        return self.server.tl.getTestCasesForTestPlan(argsAPI)
    
    def getTestCasesForTestSuite(self, testsuiteid, deep, details):
        """getTestCasesForTestSuite:
        List test cases for a test suite
        """
        argsAPI = {'devKey':self.devKey,
                 'testsuiteid':str(testsuiteid),
                 'deep':str(deep),
                 'details':str(details)}
        return self.server.tl.getTestCasesForTestSuite(argsAPI)
    
    def getTestPlanByName(self, testprojectname, testplanname):
        """getTestPlanByName
        Get info about target test plan by its name
        """ 
        argsAPI = {'devKey':self.devKey,
                'testprojectname':str(testprojectname),
                'testplanname':str(testplanname)}
        return self.server.tl.getTestPlanByName(argsAPI)
   
    def getTestPlanPlatforms(self, testplanid):
        """getTestPlanPlatforms
        Return the list of platforms associated to a given test plan
        """
        argsAPI = {'devKey':self.devKey,
                   'testplanid':str(testplanid)}
        return self.server.tl.getTestPlatforms(argsAPI)
    
    def getTestProjectByName(self, testprojectname):
        """getTestProjectByName:
        Get info about a test project by its name
        """
        argsAPI = {'devKey':self.devKey,
                 'testprojectname':str(testprojectname)}
        return self.server.tl.getTestProjectByName(argsAPI)
   
    def getTestSuiteByID(self, testsuiteid):
        """getTestSuiteByID
        Return a testsuite by ID
        """
        argsAPI = {'devKey':self.devKey,
                 'testsuiteid':str(testsuiteid)}
        return self.server.tl.getTestSuiteByID(argsAPI)
    
    def getTestSuitesForTestPlan(self, testplanid):
        """getTestSuitesForTestPlan:
        List test suites of a test plan alphabetically
        """
        argsAPI = {'devKey':self.devKey,
                 'testplanid':str(testplanid)}
        return self.server.tl.getTestSuitesForTestPlan(argsAPI)
    
    def getTestSuitesForTestSuite(self, testsuiteid):
        """getTestSuitesForTestSuite
        Get list of TestSuites which are DIRECT children of a given testsuite
        """
        argsAPI = {'devKey':self.devKey,
                 'testsuiteid':str(testsuiteid)}
        return self.server.tl.getTestSuitesForTestSuite(argsAPI)

    def getTotalsForTestPlan(self, testplanid):
        """getTotalsForTestPlan:
        Get the summarized results grouped by platform
        """
        argsAPI = {'devKey':self.devKey,
                 'testplanid':str(testplanid)}
        return self.server.tl.getTotalsForTestPlan(argsAPI)
    
    def createTestProject(self, *args):
        """createTestProject:
        Create a test project
            Mandatory parameters: testprojectname, testcaseprefix
            Optional parameters: notes, options, active, public
            Options: map of requirementsEnabled, testPriorityEnabled,
                automationEnabled, inventoryEnabled
        """
        testprojectname = args[0]
        testcaseprefix = args[1]
        options = {}
        argsAPI = {'devKey':self.devKey,
                 'testprojectname':str(testprojectname),
                 'testcaseprefix':str(testcaseprefix)}
        if len(args) > 2:
            params = args[2:]
            for param in params:
                paramlist = param.split("=")
                if paramlist[0] == 'options':
                    optionlist = paramlist[1].split(",")
                    for option in optionlist:
                        optiontuple = option.split(":")
                        options[optiontuple[0]] = optiontuple[1]
                    argsAPI[paramlist[0]] = options
                else:
                    argsAPI[paramlist[0]] = paramlist[1]
        return self.server.tl.createTestProject(argsAPI)
    
    def createBuild(self, testplanid, buildname, buildnotes):
        """createBuild:
        Create a new build for a specific test plan
        """
        argsAPI = {'devKey':self.devKey,
                 'testplanid':str(testplanid),
                 'buildname':str(buildname),
                 'buildnotes':str(buildnotes)}
        return self.server.tl.createBuild(argsAPI)
    
    def createTestPlan(self, *args):
        """createTestPlan:
        Create a test plan
            Mandatory parameters: testplanname, testprojectname
            Optional parameters: notes, active, public
        """
        testplanname = args[0]
        testprojectname = args[1]
        argsAPI = {'devKey':self.devKey,
                 'testplanname':str(testplanname),
                 'testprojectname':str(testprojectname)}
        if len(args) > 2:
            params = args[2:]
            for param in params:
                paramlist = param.split("=")
                argsAPI[paramlist[0]] = paramlist[1]
        return self.server.tl.createTestPlan(argsAPI)
    
    def createTestSuite(self, *args):
        """createTestSuite:
        Create a test suite
            Mandatory parameters: testprojectid, testsuitename, details
            Optional parameters: parentid, order, checkduplicatedname,
                                actiononduplicatedname
        """
        argsAPI = {'devKey':self.devKey,
                 'testprojectid':str(args[0]),
                 'testsuitename':str(args[1]),
                 'details':str(args[2])}
        if len(args) > 3:
            params = args[3:]
            for param in params:
                paramlist = param.split("=")
                argsAPI[paramlist[0]] = paramlist[1]
        return self.server.tl.createTestSuite(argsAPI)
    
    def createTestCase(self, *args):
        """createTestCase:
        Create a test case
            Mandatory parameters: testcasename, testsuiteid, testprojectid,
                            authorlogin, summary, steps
            Optional parameters: preconditions, importance, execution, order,
                            internalid, checkduplicatedname, actiononduplicatedname
        """
        argsAPI = {'devKey':self.devKey,
                 'testcasename':str(args[0]),
                 'testsuiteid':str(args[1]),
                 'testprojectid':str(args[2]),
                 'authorlogin':str(args[3]),
                 'summary':str(args[4]),
                 'steps':self.stepsList}
        if len(args) > 5:
            params = args[5:]
            for param in params:
                paramlist = param.split("=")
                argsAPI[paramlist[0]] = paramlist[1]
        ret = self.server.tl.createTestCase(argsAPI)
        self.stepsList = []
        return ret
    
    #
    #  ADDITIONNAL FUNCTIONS
    #                                   

    def countProjects(self):
        """ countProjects:
        Count all the test project   
        """
        projects = TestLinkClientAPI.getProjects(self)
        return len(projects)
    
    def countTestPlans(self):
        """ countProjects:
        Count all the test plans   
        """
        projects = TestLinkClientAPI.getProjects(self)
        nbTP = 0
        for project in projects:
            ret = TestLinkClientAPI.getProjectTestPlans(self, project['id'])
            nbTP += len(ret)
        return nbTP

    def countTestSuites(self):
        """ countProjects:
        Count all the test suites   
        """
        projects = TestLinkClientAPI.getProjects(self)
        nbTS = 0
        for project in projects:
            TestPlans = TestLinkClientAPI.getProjectTestPlans(self,
                                                                 project['id'])
            for TestPlan in TestPlans:
                TestSuites = TestLinkClientAPI.getTestSuitesForTestPlan(self,
                                                                TestPlan['id'])
                nbTS += len(TestSuites)
        return nbTS
               
    def countTestCasesTP(self):
        """ countProjects:
        Count all the test cases linked to a Test Plan   
        """
        projects = TestLinkClientAPI.getProjects(self)
        nbTC = 0
        for project in projects:
            TestPlans = TestLinkClientAPI.getProjectTestPlans(self,
                                                                 project['id'])
            for TestPlan in TestPlans:
                TestCases = TestLinkClientAPI.getTestCasesForTestPlan(self,
                                                                TestPlan['id'])
                nbTC += len(TestCases)
        return nbTC
        
    def countTestCasesTS(self):
        """ countProjects:
        Count all the test cases linked to a Test Suite   
        """
        projects = TestLinkClientAPI.getProjects(self)
        nbTC = 0
        for project in projects:
            TestPlans = TestLinkClientAPI.getProjectTestPlans(self,
                                                                 project['id'])
            for TestPlan in TestPlans:
                TestSuites = TestLinkClientAPI.getTestSuitesForTestPlan(self,
                                                                TestPlan['id'])
                for TestSuite in TestSuites:
                    TestCases = TestLinkClientAPI.getTestCasesForTestSuite(self,
                                                 TestSuite['id'], 'true', 'full')
                    for TestCase in TestCases:
                        nbTC += len(TestCase)
        return nbTC

    def countPlatforms(self):
        """ countPlatforms:
        Count all the Platforms  
        """
        projects = TestLinkClientAPI.getProjects(self)
        nbPlatforms = 0
        for project in projects:
            TestPlans = TestLinkClientAPI.getProjectTestPlans(self,
                                                                 project['id'])
            for TestPlan in TestPlans:
                Platforms = TestLinkClientAPI.getTestPlanPlatforms(self,
                                                                TestPlan['id'])
                nbPlatforms += len(Platforms)
        return nbPlatforms
        
    def countBuilds(self):
        """ countBuilds:
        Count all the Builds  
        """
        projects = TestLinkClientAPI.getProjects(self)
        nbBuilds = 0
        for project in projects:
            TestPlans = TestLinkClientAPI.getProjectTestPlans(self,
                                                                 project['id'])
            for TestPlan in TestPlans:
                Builds = TestLinkClientAPI.getBuildsForTestPlan(self,
                                                                TestPlan['id'])
                nbBuilds += len(Builds)
        return nbBuilds
        
    def listProjects(self):
        """ listProjects:
        List the Projects (display Name & ID)  
        """
        projects = TestLinkClientAPI.getProjects(self)
        for project in projects:
            print "Name: %s ID: %s " % (project['name'], project['id'])
  

    def initStep(self, actions, expected_results, execution_type):
        """ initStep:
        Initializes the list which stores the Steps of a Test Case to create  
        """
        self.stepsList = []
        steplist = {}
        steplist['step_number'] = '1'
        steplist['actions'] = actions
        steplist['expected_results'] = expected_results
        steplist['execution_type'] = str(execution_type)
        self.stepsList.append(steplist)
        return True
        
    def appendStep(self, actions, expected_results, execution_type):
        """ appendStep:
        Append a step to the steps list  
        """
        steplist = {}
        steplist['step_number'] = str(len(self.stepsList) + 1)
        steplist['actions'] = actions
        steplist['expected_results'] = expected_results
        steplist['execution_type'] = str(execution_type)
        self.stepsList.append(steplist)
        return True                
                                        
    def getProjectIDByName(self, projectName):   
        projects = self.server.tl.getProjects({'devKey' : self.devKey})
        for project in projects:
            if (project['name'] == projectName): 
                result = project['id']
            else:
                result = -1
        return result
    
    def reportTCResult(self, *args):
        argsAPI = {'devKey':self.devKey,
                 'testcaseid':str(args[0]),
                 'testcaseexternalid':str(args[1]),
                 'testplanid':str(args[2]),
                 'status':str(args[3])}
        if len(args) > 4:
            params = args[4:]
            for param in params:
                paramlist = param.split("=")
                argsAPI[paramlist[0]] = paramlist[1]
        return self.server.tl.reportTCResult(argsAPI)
    
    def setTestCaseExecutionResult(self, *args):
        argsAPI = {'devKey':self.devKey,
                 'testcaseid':str(args[0]),
                 'testcaseexternalid':str(args[1]),
                 'testplanid':str(args[2]),
                 'status':str(args[3])}
        if len(args) > 4:
            params = args[4:]
            for param in params:
                paramlist = param.split("=")
                argsAPI[paramlist[0]] = paramlist[1]
        return self.server.tl.setTestCaseExecutionResult(argsAPI)
    
    def addTestCaseToTestPlan(self, *args): #testprojectid, testplanid, testcaseid, version, platformid, order, urgency):
#        testcase = self.server.tl.getTestCase({'devKey':self.devKey, 'testcaseid':str(testcasevisibleid)})
#        print testcase[0]['version']
        argsAPI = {'testprojectid':str(args[0]),
                 'testplanid':str(args[1]),
                 'testcaseexternalid':str(args[2]),
                 'version':str(args[3])}
        if len(args) > 4:
            params = args[4:]
            for param in params:
                paramlist = param.split("=")
                argsAPI[paramlist[0]] = paramlist[1]
        print 'version'
        return self.server.tl.addTestCaseToTestPlan(argsAPI)
        
if __name__ == "__main__":    
    myTestLinkServer = "http://10.249.64.103/testlink/lib/api/xmlrpc.php"  #change
    myDevKey = "3fa1f1d4d63e85309f05fae3131013ea" # Put here your devKey
    myTestLink = TestLinkClientAPI(myTestLinkServer, myDevKey)
    
    if myTestLink.checkDevKey() == True:      
        methodList = [method for method in TestLinkClientAPI.__dict__]
        for method in methodList:
            if method[0:2] != "__": 
                print method
        print ""
    else:
        print "Incorrect DevKey."   
                
        
