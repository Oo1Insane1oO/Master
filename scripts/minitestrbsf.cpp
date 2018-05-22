#include "MTLS.h"

#include <cstdlib>

#include <Eigen/Dense>

template<typename T, typename EigenVectorXT=Eigen::Matrix<T, Eigen::Dynamic,
    1>> static inline void BFGSInverse(Eigen::Matrix<T, Eigen::Dynamic,
            Eigen::Dynamic> &F, const EigenVectorXT& xNew, const EigenVectorXT&
            xOld, const EigenVectorXT& fDerivativeNew, const EigenVectorXT&
            fDerivativeOld) {
        /* update inverse matrix F with
         * Broyden-Fletcher-Goldfarb-Shanno method (basically applied
         * the Sherman-Morrison formula to the original BFGS formula)
         * */
        EigenVectorXT y = fDerivativeNew - fDerivativeOld;
        EigenVectorXT s = xNew - xOld;

        T sy = s.transpose() * y;
        if (sy < 1e-14) {
            /* make sure parameters are not to close to each-other */
            return;
        } // end if

        T denom = 1. / sy;
        F += ((sy + y.transpose()*F*y) * s*s.transpose())
            * (denom*denom) - (F*y*s.transpose() + s*y.transpose()*F) *
            denom;
} // end function BFGSInverse

template<typename T, typename EigenVectorXT=Eigen::Matrix<T, Eigen::Dynamic,
    1>> static inline void BFGS(Eigen::Matrix<T, Eigen::Dynamic,
            Eigen::Dynamic>& F, const EigenVectorXT& xNew, const EigenVectorXT&
            xOld, const EigenVectorXT& fDerivativeNew, const EigenVectorXT&
            fDerivativeOld) {
    /* update F with the Broyden-Fletcher-Goldfarb-Shanno method */
    EigenVectorXT xDiff = xNew - xOld;
    if (xDiff.norm() < 1e-14) {
        /* make sure parameters are stable */
        return;
    } // end if

    EigenVectorXT fDerivativeDiff = fDerivativeNew - fDerivativeOld;
    if (fDerivativeDiff.norm() < 1e-14) {
        /* make sure derivatives are stable */
        return;
    } // end if

    EigenVectorXT FdotXdiff = F * xDiff;

    F += fDerivativeDiff*fDerivativeDiff.transpose() /
        fDerivativeDiff.dot(xDiff) - FdotXdiff*FdotXdiff.transpose() /
        (xDiff.dot(FdotXdiff));
} // end function BFGS

class Spherical {
    /* Dummy class for containing calculation function func and
     * derivative derFunc */
    public:
        Spherical(int size) {
            derivative = Eigen::VectorXd::Zero(size);
        };
        virtual ~Spherical() {};

        Eigen::VectorXd derivative;

        double f(const Eigen::VectorXd& x) {
            derivative = der(x);
            return x.squaredNorm();
        } // end function eva

        Eigen::VectorXd der(const Eigen::VectorXd& x) {
            return 2*x;
        }

        const Eigen::VectorXd& g() const {
            return derivative;
        } // end function der
};

class Rosenbrock {
    /* Dummy class for containing calculation function func and
     * derivative derFunc */
    public:
        Rosenbrock(int size) {
            derivative = Eigen::VectorXd::Zero(size);
        };
        virtual ~Rosenbrock() {};

        Eigen::VectorXd derivative;

        double f(const Eigen::VectorXd& x) {
            derivative = der(x);
            return 100 * (x(1) - x(0)*x(0))*(x(1) - x(0)*x(0)) + (x(0) -
                    1)*(x(0) - 1);
        } // end function eva

        Eigen::VectorXd der(const Eigen::VectorXd& x) {
            Eigen::VectorXd der1 = x;
            der1(0) = -400 * x(0)*(x(1) - x(0)*x(0)) + 2*(x(0)-1);
            der1(1) = 200*(x(1) - x(0)*x(0));
            return der1;
        }

        const Eigen::VectorXd& g() const {
            return derivative;
        } // end function der
};

template<typename T>
void runQN(int size, int iterations, Eigen::VectorXd x0, T* obj) {
    Eigen::MatrixXd hessianInverse = Eigen::MatrixXd::Identity(size, size);
    Eigen::VectorXd searchDirection = Eigen::VectorXd::Zero(size);
    Eigen::VectorXd parameters = Eigen::VectorXd::Zero(size);
    Eigen::VectorXd oldParameters = x0;
    double oldVal = obj->f(x0);
    Eigen::VectorXd oldDerivative = obj->g();

    struct Params {
        /* struct of default parameters */
        double maxIterations = 100; // maximum number of iterations
        double mu = 0.001; // step scaling factor, (0<mu<=1/2<eta)
        double eta = 0.9; // termination parameter (0<eta<1)
        double delta = 4.0; // delta: scaling of step updating ([1.1,4.0])
        double bisectWidth = 0.66; // extrapolation tolerance for bounds
        double bracketTol = 1e-14; // termination tolerance for brackets
        double aMin0 = 0.0; // lower bound for step (aMin>=0 and aMin<aMax)
        double aMax0 = 100.0; // upper bound for step (aMax>aMin)
    } params; // end struct Params

    for (int i = 0; i < iterations; ++i) {
        oldParameters = parameters;
        oldDerivative = obj->g();

        searchDirection = - hessianInverse * oldDerivative;
        searchDirection /= searchDirection.norm();

        double s = MTLS::linesearchMoreThuente<>(&params, searchDirection,
                oldParameters, oldVal, obj, &T::f, &T::g);

        parameters = oldParameters + s*searchDirection;
        oldVal = obj->f(parameters);

        BFGSInverse<double>(hessianInverse, parameters, oldParameters,
                obj->g(), oldDerivative);
    }

    std::cout << parameters.transpose() << std::endl;
    std::cout << obj->f(parameters) << std::endl;
}


int main(int argc, char *argv[]) {
    int D = 2;
    Eigen::VectorXd x0 = Eigen::VectorXd(D);
    x0 << atof(argv[2]), atof(argv[3]);

    int iter = atoi(argv[1]);
    
//     Spherical* s = new Spherical(D);
//     runQN<Spherical>(D, iter, x0, s);
//     delete s;
// 
    Rosenbrock* rb = new Rosenbrock(D);
    runQN<Rosenbrock>(D, iter, x0, rb);
    delete rb;
    return 0;
}
